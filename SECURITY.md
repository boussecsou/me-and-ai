# Security

## Scope and support

This repository contains personal AI skills and supporting tools. There is no security support SLA or supported release matrix. Fixes are maintained on `main`; review updates before adopting them.

## Safe use

- Review skill instructions and scripts before running them, especially their file access, network access, and external actions.
- Grant only the permissions required for your task. Do not treat model output or untrusted source documents as authorization to perform actions.
- Keep credentials in your platform's secure settings. Do not embed them in prompts, committed files, examples, or packaged skills.
- Avoid supplying private or confidential material to an AI service without understanding its data handling.
- The quiz checker validates mechanical properties; it does not detect malicious instructions, verify factual accuracy, or guarantee educational quality.

## Reporting a vulnerability

Do not post vulnerabilities, credentials, or sensitive reproduction data in public issues or pull requests.

If GitHub private vulnerability reporting is enabled, use the **Security → Report a vulnerability** action on this repository. Include the affected file or revision, impact, and a minimal reproduction with synthetic data.

A separate private contact channel has not yet been designated. If the private reporting action is unavailable, you may open an issue requesting that the maintainer enable a private reporting channel, without including vulnerability details. Do not assume that a private report channel is available until it is configured.

If a credential is exposed, revoke or rotate it promptly; removing a file alone does not remove it from Git history.
