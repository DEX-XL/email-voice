# Contributing

Useful improvements make first-time setup simpler, preserve a user's own voice, reduce repeated reading, or document a platform route with evidence.

1. Use synthetic data only. Keep personal profiles and mail outside the repository.
2. Keep the runtime package self-contained in `skills/email-voice/SKILL.md`. Change README/platform notes when behavior or compatibility changes.
3. Do not add a hard-coded person's voice, English-only assumption, universal greeting, em-dash ban or other personal preference.
4. Do not claim native installation, connector availability, automatic model switching, guaranteed savings or writing-quality scores without a reproducible test and appropriate scope.
5. Add a behavioral scenario when changing an important decision, and describe the observed result rather than checking for exact prose.
6. Run `python tools/build.py` and `python -m unittest discover -s tests -v`. Commit regenerated distribution files with the source change.
7. Explain the problem, change and validation in your pull request. Report which model and surface were actually tested; docs review is not a live compatibility test.

Small, focused contributions are easiest to review. Translation and regional-email examples are welcome when synthetic and clearly labeled. Do not add runtime dependencies merely to package Markdown.
