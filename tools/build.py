"""Build/check the public, one-file skill. Python standard library only."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/email-voice/SKILL.md')
SOURCE_FILES = (
    'README.md', 'LICENSE', '.gitignore', '.gitattributes', 'SECURITY.md', 'CONTRIBUTING.md',
    'CHANGELOG.md', 'skills/email-voice/SKILL.md', 'docs/COMPATIBILITY.md',
    'docs/MODELS.md', 'docs/PUBLISHING.md', 'evals/README.md', 'evals/cases.json',
    'evals/RESULTS.md', 'tools/build.py', 'tests/test_release.py',
    '.github/ISSUE_TEMPLATE/bug_report.md',
    '.github/ISSUE_TEMPLATE/compatibility_report.md',
    '.github/pull_request_template.md', '.github/workflows/check.yml',
)
DIST_FILES = ('email-voice.zip', 'email-voice.txt', 'SHA256SUMS')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def privacy_check(text: str, label: str) -> None:
    """Catch common accidental private data. Not a proof of anonymization."""
    for address in re.findall(r'[\w.+-]+@([\w.-]+\.[A-Za-z]{2,})', text):
        if not (address.lower() in {'example.com', 'example.org', 'example.net'}
                or address.lower().endswith(('.invalid', '.test'))):
            raise ValueError(f'{label}: non-synthetic email address')
    if re.search(r'[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]|/Users/[^/\s]+/|/home/[^/\s]+/', text):
        raise ValueError(f'{label}: personal absolute path')
    if re.search(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{20,}|\bsk-[A-Za-z0-9]{20,}', text):
        raise ValueError(f'{label}: possible credential')


def validate_skill(text: str) -> None:
    # A deliberately narrow parser for this project's flat scalar frontmatter.
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('Missing LF-delimited YAML frontmatter')
    fields = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(': ')
        if not sep or key in fields:
            raise ValueError('Unsupported or duplicate frontmatter field')
        fields[key] = value.strip()
    if set(fields) != {'name', 'description', 'license'}:
        raise ValueError('Unexpected/missing frontmatter fields')
    if fields['name'] != 'email-voice' or fields['license'] != 'MIT':
        raise ValueError('Skill name/license mismatch')
    if not 20 <= len(fields['description']) <= 200:
        raise ValueError('Description must fit the documented 200-character Claude limit')
    if len(text.splitlines()) > 500:
        raise ValueError('Entrypoint exceeds this project\'s 500-line bound')
    if re.search(r'\]\((?:examples|templates|references)[^)]*\)', text):
        raise ValueError('Single-file skill refers to an unbundled resource')
    privacy_check(text, 'SKILL.md')


def skill_bytes(root: Path) -> bytes:
    folder = root / SKILL.parent
    paths = list(folder.rglob('*'))
    if any(p.is_symlink() for p in paths):
        raise ValueError('Runtime skill directory contains a symlink')
    if {p.relative_to(folder).as_posix() for p in paths if p.is_file()} != {'SKILL.md'}:
        raise ValueError('Runtime package must contain exactly SKILL.md')
    data = (root / SKILL).read_bytes()
    text = data.decode('utf-8')
    if '\r' in text:
        raise ValueError('Use LF endings for reproducible cross-platform packaging')
    validate_skill(text)
    return data


def zipped(data: bytes) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', zipfile.ZIP_STORED) as z:
        info = zipfile.ZipInfo('email-voice/SKILL.md', date_time=(2026, 1, 1, 0, 0, 0))
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        info.compress_type = zipfile.ZIP_STORED
        z.writestr(info, data)
    return stream.getvalue()


def artifacts(root: Path) -> dict[str, bytes]:
    data = skill_bytes(root)
    outputs = {'email-voice.zip': zipped(data), 'email-voice.txt': data}
    outputs['SHA256SUMS'] = ''.join(f'{digest(v)}  {k}\n' for k, v in outputs.items()).encode()
    return outputs


def check_sources(root: Path) -> None:
    for name in SOURCE_FILES:
        p = root / name
        if not p.is_file() or p.is_symlink():
            raise ValueError(f'Missing or symlinked public source: {name}')
        text = p.read_text(encoding='utf-8')
        # Pattern definitions and deliberately rejected test strings in Python
        # are code, not a corpus of user-facing mail or documentation.
        if not name.endswith('.py'):
            privacy_check(text, name)
        if name.endswith('.md'):
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in link or link.startswith('#'):
                    continue
                target = link.split('#', 1)[0]
                if target and not (p.parent / target).exists():
                    raise ValueError(f'{name}: broken local link {target}')
    cases = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))
    if len({c['id'] for c in cases}) != len(cases):
        raise ValueError('Duplicate evaluation IDs')


def build(root: Path = ROOT, check: bool = False) -> dict:
    outputs = artifacts(root)
    dist = root / 'dist'
    if check:
        for name, data in outputs.items():
            if not (dist / name).is_file() or (dist / name).read_bytes() != data:
                raise ValueError(f'Stale or missing dist/{name}; run python tools/build.py')
    else:
        dist.mkdir(parents=True, exist_ok=True)
        for name, data in outputs.items():
            (dist / name).write_bytes(data)
    check_sources(root)
    with zipfile.ZipFile(io.BytesIO(outputs['email-voice.zip'])) as z:
        if z.namelist() != ['email-voice/SKILL.md'] or z.testzip() is not None:
            raise ValueError('Unexpected ZIP contents/integrity failure')
        if z.read(z.namelist()[0]) != (root / SKILL).read_bytes():
            raise ValueError('ZIP content differs from source')
    return dict(mode='check' if check else 'build', source_files=len(SOURCE_FILES),
                skill_bytes=len(outputs['email-voice.txt']),
                zip_bytes=len(outputs['email-voice.zip']),
                zip_sha256=digest(outputs['email-voice.zip']), runtime_files=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify committed artifacts without modifying them')
    args = parser.parse_args()
    try:
        print(json.dumps(build(check=args.check), indent=2))
    except (ValueError, OSError, UnicodeError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
