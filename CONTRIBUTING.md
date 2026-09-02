# Contributing to Radius Red

Radius Red Ltd. is a UK-based, agentic engineering company. This GitHub
organisation hosts the open-source tools and shared automation we maintain in
public; the [organisation profile](profile/README.md) says how we work.

## What this repository holds

`.github` is the organisation's shared-asset repository. It holds only what
other repositories consume:

- `.github/workflows/reusable-release.yml` and
  `.github/workflows/reusable-finalize-release.yml` — the reusable release
  workflows, called by
  [`tradedesk`](https://github.com/radiusred/tradedesk) and
  [`tradedesk-dukascopy`](https://github.com/radiusred/tradedesk-dukascopy)
  from their `prepare-release` and `finalize-release` workflows.
- `.github/actions/calculate_version` — the version-calculation action the
  release workflow runs.
- `profile/` — the organisation profile shown at
  [github.com/radiusred](https://github.com/radiusred).

Nothing else lives here. Each project's documentation lives with the project.

## Contributing to a project

Contributions are accepted per project. Every public repository carries its
own `README.md` and, where the project takes contributions, a
`CONTRIBUTING.md`; follow those. The current list is at
[github.com/orgs/radiusred/repositories](https://github.com/orgs/radiusred/repositories).

If you are unsure whether a change is wanted, open an issue in the repository
concerned describing the goal before writing the code.

## Changing this repository

`main` is protected: changes arrive by pull request, history is linear (rebase
only, no merge commits), and commit messages follow
[Conventional Commits](https://www.conventionalcommits.org/).

- Callers reference the reusable workflows and the action at `@main`, so a
  merge here is live for every caller at once. Say in the PR which callers you
  checked, and keep workflow inputs, secrets and outputs backward compatible
  or land the callers' change alongside.
- Keep the profile accurate; it is what a visitor to the organisation sees
  first.
- Never include secrets or internal data in a public PR.

## Security

To report a vulnerability in any Radius Red project, email
[opensource@radiusred.uk](mailto:opensource@radiusred.uk) rather than opening
a public issue.

---

## License

Licensed under the Apache License, Version 2.0.
See: https://www.apache.org/licenses/LICENSE-2.0

Copyright 2026 [Radius Red Ltd.](https://www.radiusred.uk)
