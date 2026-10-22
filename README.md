# Email Voice

### Teach your AI how you email.

One file that learns your writing style from your sent emails and turns it into a private, reusable writing profile. Draft replies in your voice across different AI assistants, without rebuilding your preferences in every chat.

**One skill file · One upload ZIP · MIT licensed · No bundled credentials or runtime dependencies**

**[Download the skill ZIP](https://github.com/DEX-XL/email-voice/releases/download/v0.1.0/email-voice.zip)** · [Read the single file](skills/email-voice/SKILL.md) · [Release notes](https://github.com/DEX-XL/email-voice/releases/tag/v0.1.0)

## Start in three steps

1. Download **[email-voice.zip](https://github.com/DEX-XL/email-voice/releases/download/v0.1.0/email-voice.zip)**. This is the skill package; GitHub's **Code > Download ZIP** downloads the whole source repository instead. A source-tree copy is also available in [dist](dist/email-voice.zip).
2. Add it using your assistant's supported skill flow. If it only accepts a single file, extract the ZIP and use **[SKILL.md](skills/email-voice/SKILL.md)**. No appendices need to be merged.
3. Say:

> Learn my email voice using my connected Sent mail. Use Balanced mode, recommend an efficient model, and save a private profile I can reuse. Keep email access read-only.

The assistant checks the available sources, asks only for missing setup details, samples your own writing, and builds your profile. If no mailbox connection exists, supply a Sent-only export or pasted examples instead.

**Using a coding agent?** With Node.js 22.20+ installed, Vercel's optional Skills CLI can copy Email Voice into your current project:

```bash
npx skills@1.7.4 add DEX-XL/email-voice --skill email-voice --agent codex --copy
```

For Claude Code, replace `codex` with `claude-code`. Review the displayed destination before accepting. This installs the instructions; email access still needs your host's connector or supplied samples. The Codex copy route was tested on Windows with Skills CLI 1.7.4, and the installed file matched the release checksum. This is not a live mailbox test. [CLI documentation and telemetry controls](https://github.com/vercel-labs/skills#telemetry)

**Your first useful result:** a writing-pattern summary, a private single-file profile, and an honest validation report. Quick mode uses a smaller sample; Balanced is the recommended starting point. There is no promised completion time or fixed credit cost.

## Try a synthetic example first

After loading the skill, paste this prompt. It needs no mailbox connection and contains no real correspondence:

```text
Use only these two synthetic sent examples for a tiny provisional profile.
Sender: Alex. Recipient: a familiar colleague. Language: English.

Example 1:
Hi Jordan,
Could you send the updated forecast by Wednesday? I need it for the review.
Best,
Alex

Example 2:
Hi Morgan,
Tuesday at 10 works for me. Please send the meeting link when it is ready.
Best,
Alex

Summarize the observed style, then draft a reply to Jordan confirming that
Friday at 11 works. That time is confirmed. Do not invent a time zone or
an attachment. Mark the profile provisional and do not claim validation.
```

This demonstrates the flow with supplied text. A real profile should use a broader authorized sample across your own contexts.

## What you can ask

| Say this | What happens |
|---|---|
| "Learn my email voice" | Learn greetings, length, tone, structure, closings and phrasing by recipient and purpose. |
| "Use Quick mode" | Build a provisional profile from 40 training emails and up to five reserved replies. |
| "Reply to this in my voice" | Draft from your profile and the current thread. |
| "Make this sound like me" | Edit wording while preserving the supplied facts. |
| "Refresh using my recent Sent mail" | Update from new authorized samples and show material changes. |
| "Export my style" | Get a single private Markdown skill for reuse in another assistant. |
| "Review my inbox priorities" | Produce a read-only list of threads and suggested actions if the host has access. |

## One ZIP, honest platform support

The same file contains the full workflow. Installation and persistence are controlled by the host, and email connections must be configured separately. **The Codex project copy route has been tested on Windows; other platform routes are documentation findings. Live email connector workflows have not been tested.**

| Platform | Route | Evidence/status |
|---|---|---|
| Claude / Cowork | Upload the ZIP in **Customize > Skills > + > Create skill > Upload a skill**, then enable it. A proposal card requires Save. | Native upload is documented. |
| ChatGPT desktop / Codex | Use the supported skill creation/import or local skill flow. In Codex, put the extracted email-voice folder under `~/.agents/skills/` or your project's `.agents/skills/`. | Standalone/local skills are documented. ZIP import UI depends on the surface. |
| ChatGPT web/mobile | Use supported workspace/plugin skill controls where available, or attach/paste SKILL.md as instructions for the conversation. | Do not assume every account exposes a standalone ZIP importer. |
| Gemini | Paste the Markdown body into a Gem's instructions; add your private profile as knowledge if appropriate and save. | Gems are documented; a generic Agent Skills ZIP importer is not established here. Google has announced a personal-account transition starting November 2026; check the current UI. |
| Meta Muse agent | Provide the file as task instructions using the attachment/file mechanism your account exposes. Request a supported persistent save if available. | Meta documents agent/app access; a custom SKILL.md ZIP import path was not verified. |
| Other assistants | Extract SKILL.md and supply its body as reusable instructions where supported. | Requires instruction-following and access to your supplied mail or connector. |

If ZIP uploads are unsupported, open SKILL.md and copy the text after its initial frontmatter into the host's instruction field. Keep the final embedded license when redistributing the file.

[Detailed platform notes and official sources](docs/COMPATIBILITY.md)

## Use this setup prompt

```text
Read Email Voice from the attached ZIP or SKILL.md and follow it for this task.
Help me learn my own email style, using only the Sent accounts/files I authorize.
Recommend Sol or Sonnet if available, with medium/standard effort for analysis.
Offer Quick, Balanced or Deep sampling. Build a private portable profile, test
it on reserved real replies where possible, and help me reuse it. Keep email
access read-only. If persistence needs a save/upload step, explain it and do
not claim installation until the host confirms it.
```

## Built for useful results, with a bounded budget

| Mode | Training emails | Reserved test replies | When to use |
|---|---:|---:|---|
| Quick | 40 | 5 | Try it with a modest sample; some contexts will remain unverified. |
| Balanced | 150 | 12 | Recommended starting point for a reusable profile. |
| Deep | 300 | 15 | Broader context coverage when enough qualifying mail exists. |

These are targets, not requirements to scrape indefinitely. The skill batches body reads, deduplicates messages, limits metadata scanning, saves resumable progress where possible, and stops at the selected scope. A missing family, client or academic category is marked unverified rather than blocking setup.

**Model guidance:** use an available **Sol or Sonnet** for the learning pass, with medium/standard effort where supported. Routine extraction or short replies can use a lower effort. Premium models such as Astra/Opus are optional. This recommendation does not change the model, bypass usage limits, promise a fixed savings percentage or require an API subscription. [Model and cost notes](docs/MODELS.md)

## Your voice, not someone else's rules

Some people write a warm paragraph; others answer in one line. Some use formal titles, emoji, regional expressions, multiple languages or a different signature on each account. Email Voice learns those distinctions.

You can add firm preferences such as "no em dashes," "use my first name with colleagues," or "make routine replies shorter." Explicit preferences override old mail. An absent phrase is reported as unobserved in the sample rather than something you never say.

## Privacy and data flow

The public ZIP contains instructions only. It contains no personal email corpus, connector, API key, tracking code, network client or analytics. Your assistant and its email connector process the data you authorize under their own terms and privacy controls. This is not a promise of local-only processing.

Raw mail and learned profiles stay out of the public repository. Default profile exports use aggregate patterns and deidentified phrases. Sending emails, changing labels, archiving and deleting require a separate action request. [Privacy and security](SECURITY.md)

## What is actually tested?

The repository includes synthetic evaluation scenarios for setup, drafting, multilingual style, missing data, model limitations, prompt injection and mailbox actions. Release checks verify the one-file ZIP, round-trip contents, distribution allowlist, checksums and accidental private-data patterns. These checks do not prove writing quality or a successful installation in every app.

Profiles learned by the skill are evaluated on reserved real replies where available. Scores are disclosed as agent-assessed, with a bounded revision budget and no guarantee of indistinguishable authorship. [Evaluation guide](evals/README.md)

## For contributors

Python 3.10+ is needed only to build/check the open-source release, not to use the uploaded skill.

```bash
python tools/build.py
python -m unittest discover -s tests -v
```

The build produces `dist/email-voice.zip`, a plain-text `dist/email-voice.txt` fallback, and `dist/SHA256SUMS`. The ZIP contains exactly:

```text
email-voice/
└── SKILL.md
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a change. Use synthetic mail in issues and tests. Platform reports should identify the product/surface and distinguish documented support from a successful live test.

## Publishing

Fork and adapt the skill using [the publishing checklist](docs/PUBLISHING.md). Setup reports, synthetic examples and clear platform findings are especially useful contributions. If Email Voice helps you, a GitHub star helps others discover it.

## License

[MIT](LICENSE). Created by Rohit Motwani. Independent community project; not affiliated with OpenAI, Anthropic, Google or Meta. Product names belong to their respective owners.
