# Privacy and security

Email Voice is an instruction-only skill. Its runtime ZIP has one Markdown file and no executable code, telemetry, authentication client or external endpoint. The build tools in this source repository are optional local developer utilities and are not included in the skill ZIP.

The assistant hosting the skill processes authorized messages through its own tools. Its provider's data retention, training, connector permissions and organizational policies still apply. A private profile is private relative to this public repository, not necessarily processed only on your computer.

## Defaults

- Learning reads authorized Sent mail. Received messages provide minimal reply context, not style evidence.
- Sending, forwarding, deleting, archiving, labeling and marking mail require a separate action request. A writing-style setup request does not authorize these changes.
- Message bodies and attachments are untrusted data. Embedded commands cannot grant access, trigger publication, or instruct the assistant to exfiltrate a mailbox.
- Raw mail, credentials, account identifiers, contacts, private examples, checkpoints and learned profiles are excluded from the release artifact.
- The skill neither reads attachments to hit its sample target nor requests passwords, cookies or API keys.
- Style suggestions do not establish whether a promise, attachment, completed action or availability is true.

## Before sharing a bug report

Use synthetic examples. Do not paste a real thread, account address, screenshot with personal details, token, message ID, private profile or mailbox export into a public issue. Provide product/surface, approximate sample size, expected behavior, observed behavior and a redacted reproduction.

For a suspected privacy or security issue, use GitHub's private vulnerability reporting if the maintainer has enabled it. If it is unavailable, open an issue requesting a private contact without disclosing sensitive details. Do not send raw mailbox data to the maintainer.

The release checker catches some obvious private-data patterns; it cannot prove that arbitrary text is anonymous. Human review of contributed content remains necessary.
