# Model and usage guidance

Email Voice recommends an efficient starting point because body reads and repeated context can dominate usage. The skill cannot change your selected model, subscription, credits, thinking controls or connector limits.

| Stage | Practical starting point | How to keep it bounded |
|---|---|---|
| Learning a profile | Available Sol or Sonnet, medium/standard effort if exposed | Balanced sample; bodies read once in batches. |
| Basic extraction / short replies | Same model at low effort, if supported and adequate | Use the current profile and thread rather than rescanning Sent. |
| Difficult conflicting style evidence | Medium first; optional stronger final review | Change only when a concrete quality problem warrants it. |
| Gemini / Meta Muse | Available standard/efficient host model | Do not assume third-party model names or effort controls exist. |

These are this project's suggested starting settings, not a cross-provider performance benchmark. Opus/Astra or another premium tier can help in some cases, but is not required. Model availability and cost vary by account, context size and product; subscription credits are not interchangeable with API token pricing.

## Defaults that actually reduce repeated work

- Quick: 40 training + 5 test replies. Balanced: 150 + 12. Deep: 300 + 15.
- Prefer the last 12 months; extend to 18 if the sample needs it.
- Scan metadata before bodies where supported. Stop at five times the desired total unless the user expands the scope.
- Read bodies in batches of about 20, deduplicate across accounts and reuse cleaned text.
- Keep all messages in reserved conversations out of the training set.
- Store a private checkpoint where possible and resume it after interruptions.
- Include at most one revision and one retest in the default validation budget.
- Stop at observed usage limits; deliver a provisional result instead of retrying indefinitely.
- Routine drafting reads the compact profile and the current thread, not hundreds of old messages.

No fixed dollar cost, credit estimate, percentage saving or runtime is promised. The host can expose actual usage, but the skill must not invent it when unavailable.

## Settings that are not universal

Some apps hide effort controls; some models reject arbitrary temperature values; some services choose their own model. This skill therefore has no `model:` frontmatter, model-switching script or hard-coded temperature. Choose settings using the host UI or its documented controls. The user remains in charge.

## Sources

Reviewed 21 October 2026:

- [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection): tradeoffs depend on task and effort; evaluate the lightest setting that meets your needs.
- [Anthropic models](https://platform.claude.com/docs/en/models/overview): Sonnet is positioned for speed/intelligence; available models and prices change over time.
- [Google Gems](https://support.google.com/gemini/answer/15146780?hl=en) and [Meta Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/): host-specific workflows should not be presented as universal third-party model controls.
