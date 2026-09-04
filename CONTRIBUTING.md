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
- `.github/actions/commitlint` — the shared commit-message lint action, with
  the organisation's `commitlint.config.mjs` inside it. Any repository that
  lints commit messages calls it from a thin workflow (see
  [Linting commit messages in a repository](#linting-commit-messages-in-a-repository));
  this repository's own `.github/workflows/commitlint.yml` is the reference
  caller.
- `profile/` — the organisation profile shown at
  [github.com/radiusred](https://github.com/radiusred).

Beyond those, the repository carries only its own housekeeping: this file,
`.gitignore`, `.codecrew.yml`, which points CodeCrew coordination for this
repository at the company hub, and `.github/workflows/commitlint.yml`, its own
call of the shared commit lint. Each project's documentation lives with the
project.

## Contributing to a project

Contributions are accepted per project. Each project repository carries its
own `README.md` and, where the project takes contributions, a
`CONTRIBUTING.md`; follow those. The current list is at
[github.com/orgs/radiusred/repositories](https://github.com/orgs/radiusred/repositories).
(This repository is not a project: `profile/README.md` is the organisation
profile GitHub shows on the org page, not a repository README, and this file
is its contributing guide.)

If you are unsure whether a change is wanted, open an issue in the repository
concerned describing the goal before writing the code.

## Linting commit messages in a repository

Every Radius Red repository lints pull-request commit messages against
[Conventional Commits](https://www.conventionalcommits.org/) through the
shared action in this repository, so the config and the pinned
`wagoid/commitlint-github-action` version change in one place. Do not add a
`commitlint.config.mjs` to the calling repository; the action carries it.

Copy this file to `.github/workflows/commitlint.yml` in the repository:

```yaml
name: Lint commit messages

on:
  pull_request:

permissions:
  contents: read
  pull-requests: read

jobs:
  commitlint:
    name: Lint commit messages
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: radiusred/.github/.github/actions/commitlint@main
```

- **The job name must be exactly `Lint commit messages`.** It is the check
  context the organisation ruleset `require-lint` requires on the default
  branch of every public repository; a job named anything else reports a
  different context, and pull requests cannot merge until a check with the
  required one passes. (This is why the shared piece is a composite action
  rather than a reusable workflow: GitHub reports a called workflow's job as
  `caller job / called job`, which can never equal the required context.)
- **Permissions.** `contents: read` is for the checkout. `pull-requests: read`
  lets the action list the pull request's commits; a private repository
  fails without it, a public one merely gets it for free. Keep both.
- **The action does not check out.** Run `actions/checkout` with
  `fetch-depth: 0` before it, as above.
- This repository calls the action by local path (`./.github/actions/commitlint`)
  instead of `@main`, so a pull request here tests the version of the action
  it carries. Every other repository uses `@main`.

## Changing this repository

`main` is protected: changes arrive by pull request, history is linear (rebase
only, no merge commits), and commit messages follow
[Conventional Commits](https://www.conventionalcommits.org/).

- Callers reference the reusable workflows and the actions at `@main`, so a
  merge here is live for every caller at once. Say in the PR which callers you
  checked, and keep workflow inputs, secrets and outputs backward compatible
  or land the callers' change alongside. A change to the commitlint config or
  to the pinned `wagoid/commitlint-github-action` version is proved by this
  repository's own `Lint commit messages` check before it can merge.
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
