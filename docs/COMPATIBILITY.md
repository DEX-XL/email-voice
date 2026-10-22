# Platform compatibility

Checked against official documentation on **21 October 2026**. These are documentation findings, not a claim of live end-to-end testing on each account, plan or device. Email Voice is an instruction file; account access and persistence remain host features.

## Claude and Cowork

1. Download `dist/email-voice.zip`.
2. Open **Customize > Skills > + > Create skill > Upload a skill**.
3. Upload the ZIP and enable it. If a conversation instead proposes a save card, click Save and verify the skill appears in the host's list.
4. Ask to learn your email voice. Connect an email account through the host's supported flow or supply a Sent export.

The ZIP contains a folder named `email-voice` with one `SKILL.md`. All instructions and the license are inside that file. A single-file creator can use SKILL.md directly without merging references.

Sources: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Skills require code execution and may be governed by organization settings.

## ChatGPT and Codex

Standalone skills are documented for the ChatGPT desktop app, Codex CLI and IDE extension. Skills bundled in plugins have broader surface availability. This release is a standalone skill, not a submitted plugin or a marketplace listing.

In a supported local environment, extract the `email-voice` directory into your user's `~/.agents/skills/`, or into a project's `.agents/skills/`. Use the actual host's supported location if it differs. In Codex invoke `$email-voice`; supported ChatGPT skill surfaces use `@` selection. An ordinary chat can instead read the extracted Markdown as task instructions if file upload/paste is available. Do not call this a permanent installation unless the host saves and enables it.

Sources: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins), [Skill distribution boundaries](https://learn.chatgpt.com/docs/enterprise/skills).

### Optional coding-agent installer

Vercel's Skills CLI discovers `skills/email-voice/SKILL.md` directly from this public repository. With Node.js 22.20+ installed, run from the project where you want the skill:

```bash
npx skills@1.7.4 add DEX-XL/email-voice --skill email-voice --agent codex --copy
```

Review and accept the displayed project destination. For Claude Code, use `--agent claude-code`; that destination is documented by the CLI but was not live-tested here. The ZIP remains the route for Claude's native upload interface. These are different installation surfaces.

On 21 October 2026 (America/New_York), the maintainer tested discovery and a noninteractive Codex copy installation with CLI 1.7.4 on Windows in an isolated project. The installed SKILL.md had SHA-256 `88967d8e68175f82e5eb7fbe21bc7fd22c4f0825f53b63e0379e28e1d8d2bef6`, matching v0.1.0. No mail was read during this check. The CLI has its own telemetry and security-audit behavior; its documentation describes `DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` controls. Email Voice itself contains no telemetry.

Sources: [Skills CLI installation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [repository discovery](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md), [CLI telemetry](https://github.com/vercel-labs/skills#telemetry).

## Gemini

Google documents creating a Gem with a name and instructions, optional knowledge files and a Save step. Extract SKILL.md, paste its Markdown body into the Gem instructions, save, and supply your private profile as context when available. If an instruction length limit prevents this, use the file as knowledge plus a short instruction to follow it; confirm the host can actually read that file before proceeding.

This review did not establish an Agent Skills ZIP importer for the current Gemini consumer surface. Google announces that personal-account Gems start transitioning to skills in November 2026, so check the current product UI rather than assuming the October route will remain unchanged. Work/school policies can differ.

Sources: [Use Gems](https://support.google.com/gemini/answer/15146780?hl=en), [Get started with Gems](https://support.google.com/gemini/answer/15236321?hl=en).

## Meta Muse agent

This means Meta's personal Muse agent, not another product with a similar name. Meta documents connected apps, task execution and a persistent secure VM. The official materials reviewed did not establish a user-facing custom SKILL.md ZIP importer or a user-selectable Sol/Sonnet model.

Provide the file using your account's supported attachment/file route, or paste its instructions. Ask Muse to follow it for the current task and save a private reusable profile if that capability is available. If the host cannot read the ZIP, use the extracted file/text. Confirm any persistent save in the product; do not invent a file path, installation menu or model control.

Sources: [Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), [Muse capabilities](https://ai.meta.com/muse/).

## General fallback

One source file can travel between assistants even when installation mechanisms differ:

1. Extract the ZIP.
2. Give the host SKILL.md, or copy its Markdown body after the initial YAML frontmatter.
3. Ask it to follow Email Voice for this task.
4. Connect a supported mailbox or supply your own Sent samples.
5. Save the resulting private profile and reattach it when moving to another host.

A file upload is not a guarantee of persistent memory, email access, native skill installation, model availability or identical model behavior. Please contribute a synthetic-data live test report if your surface works differently.
