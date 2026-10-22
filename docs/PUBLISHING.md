# Publish and launch Email Voice

## Prepare the public repository

The repository is intended to contain only the generic skill, documentation, synthetic evaluation scenarios, build tools and release artifacts. Never publish the private source emails or personalized skill used to inspire it.

1. Run `python tools/build.py` and `python -m unittest discover -s tests -v`.
2. Review the allowlisted source files and the ZIP's sole entry, `email-voice/SKILL.md`.
3. Confirm that `dist/SHA256SUMS` matches the ZIP and plain-text fallback.
4. Create a public repository named `email-voice` under your chosen GitHub account. Do not upload the parent workspace or private training directory.
5. Push this repository only. Enable Issues and private vulnerability reporting if available and appropriate.
6. Create a `v0.1.0` release, attach `dist/email-voice.zip`, `dist/email-voice.txt`, and `dist/SHA256SUMS`, and include the limitations below.
7. Replace relative download links with a release-asset link only after that release actually exists. Keep the relative links usable for source downloads.

## Suggested repository metadata

**Description:** Learn your email voice from sent mail. One-file AI skill with private profiles, budget-aware sampling, and portable instructions.

**Topics:** `agent-skills`, `email`, `writing-assistant`, `claude`, `codex`, `chatgpt`, `gemini`, `personalization`, `productivity`, `prompt-engineering`.

Do not add fake install counts, testimonials, compatibility badges, benchmarks or stars. Use a verified live URL in announcements. If no repository is published yet, keep outreach as a draft.

## Demo that helps people decide

Use only synthetic mail:

1. Show the single-file import and visible save/enable result on a tested surface.
2. Choose Quick mode and a synthetic Sent sample with two different recipient contexts.
3. Show the resulting profile and one draft before/after a user correction.
4. Show how to save a private single-file export and use it in another host.
5. State that the host supplies email access, model settings are recommendations, and cross-platform installation is not identical.

Ask testers: Which app/model? Was setup clear? Could it read the file? Did the greeting/signature fit? Did it stop at the chosen scope? Did it invent facts? Avoid collecting their real emails or profiles.

## Short launch description

> I built Email Voice, an open-source, one-file skill that helps an AI learn your writing habits from your own sent emails. It creates a private portable style profile, then uses it for drafts and replies. It supports connected mail or supplied samples, has bounded sampling modes, and recommends efficient models such as Sol/Sonnet where available. Installation depends on the host; the README explains native and instruction-based routes. I'd value feedback on setup and the quality of the first draft.

## Sharing responsibly

Start with people who want to try it. Ask for feedback rather than demanding a star. On Reddit, read the exact community rules and use permitted project/self-promotion threads with creator disclosure. Do not repeatedly paste promotional replies, evade a removal, or buy/fabricate engagement. A useful release, a clear demo and responsive issue handling are within the maintainer's control; reaching a star target is not guaranteed.

Track actual repository stars and the date observed, completed installations reported by testers, useful feedback and resolved issues. Distinguish a request sent from a test completed. Do not infer endorsements from a click or a group message.
