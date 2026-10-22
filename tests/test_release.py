import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('release', ROOT / 'tools/build.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_archive_is_one_file_and_exact_source(self):
        outputs = release.artifacts(ROOT)
        with zipfile.ZipFile(io.BytesIO(outputs['email-voice.zip'])) as z:
            self.assertEqual(z.namelist(), ['email-voice/SKILL.md'])
            self.assertEqual(z.read(z.namelist()[0]), (ROOT / release.SKILL).read_bytes())
            self.assertIsNone(z.testzip())

    def test_build_is_deterministic(self):
        self.assertEqual(release.artifacts(ROOT), release.artifacts(ROOT))

    def test_checksums_match_outputs(self):
        outputs = release.artifacts(ROOT)
        for line in outputs['SHA256SUMS'].decode().splitlines():
            sha, name = line.split('  ')
            self.assertEqual(sha, release.digest(outputs[name]))

    def test_unexpected_runtime_file_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix='.test-', dir=ROOT) as temp:
            root = Path(temp)
            self.assertEqual(root.resolve().parent, ROOT.resolve())
            folder = root / release.SKILL.parent
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_bytes((ROOT / release.SKILL).read_bytes())
            (folder / 'mailbox.json').write_text('private message')
            with self.assertRaisesRegex(ValueError, 'exactly SKILL'):
                release.artifacts(root)

    def test_private_sibling_is_not_packaged(self):
        with tempfile.TemporaryDirectory(prefix='.test-', dir=ROOT) as temp:
            root = Path(temp)
            self.assertEqual(root.resolve().parent, ROOT.resolve())
            folder = root / release.SKILL.parent
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_bytes((ROOT / release.SKILL).read_bytes())
            (root / 'private-mail.txt').write_text('Never distribute this message')
            with zipfile.ZipFile(io.BytesIO(release.artifacts(root)['email-voice.zip'])) as z:
                self.assertNotIn(b'Never distribute', z.read('email-voice/SKILL.md'))

    def test_personal_address_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'non-synthetic'):
            release.privacy_check('person@actual-mail-provider.com', 'test')

    def test_reserved_synthetic_address_is_allowed(self):
        release.privacy_check('alex@example.com and sam@company.test', 'test')

    def test_personal_absolute_path_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'absolute path'):
            release.privacy_check('/home/alex/private/mail.mbox', 'test')

    def test_private_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'credential'):
            release.privacy_check('-----BEGIN PRIVATE KEY-----', 'test')

    def test_wrong_skill_name_is_rejected(self):
        text = (ROOT / release.SKILL).read_text(encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'name/license'):
            release.validate_skill(text.replace('name: email-voice', 'name: someone-else', 1))

    def test_duplicate_frontmatter_is_rejected(self):
        text = (ROOT / release.SKILL).read_text(encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            release.validate_skill(text.replace('license: MIT', 'license: MIT\nname: email-voice', 1))

    def test_distribution_is_current(self):
        self.assertEqual(release.build(ROOT, check=True)['runtime_files'], 1)


if __name__ == '__main__':
    unittest.main()
