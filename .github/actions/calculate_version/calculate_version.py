#!/usr/bin/env python3

import subprocess
import os
import re
import tomllib

BREAKING_HEADER_RE = re.compile(r"^[a-z]+(\([^)]+\))?!:")
FEAT_RE = re.compile(r"^feat(\([^)]+\))?:", re.IGNORECASE)
RELEASE_COMMIT_RE = re.compile(r"^chore: release v(\d+\.\d+\.\d+)$")


def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True).strip()


def existing_release_tag() -> str | None:
    """If HEAD is already a `chore: release vX.Y.Z` bump commit, return that
    tag so re-runs of Prepare-Release are idempotent. Without this, a re-run
    after a manually-merged release PR re-bumps the version a second time
    (e.g. v0.5.0 already on main → calculator returns v0.6.0)."""
    head_msg = run("git log -1 --pretty=%s")
    m = RELEASE_COMMIT_RE.match(head_msg)
    if not m:
        return None
    return f"v{m.group(1)}"


def get_current_version() -> str:
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    version_file = data["tool"]["hatch"]["version"]["path"]
    content = open(version_file).read()
    m = re.search(r'__version__\s*=\s*"([^"]+)"', content)
    if not m:
        raise ValueError(f"No __version__ found in {version_file}")
    return m.group(1)


def bump_version(version: str, bump: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    if bump == "major":
        return f"{major + 1}.0.0"
    elif bump == "minor":
        return f"{major}.{minor + 1}.0"
    else:
        return f"{major}.{minor}.{patch + 1}"


def main() -> None:
    summary_path = os.environ["GITHUB_STEP_SUMMARY"]
    output_path = os.environ["GITHUB_OUTPUT"]

    existing_tag = existing_release_tag()
    if existing_tag is not None:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(f"### Release Plan for {os.environ['GITHUB_REPOSITORY']}\n")
            f.write(
                f"* HEAD already contains release bump `{existing_tag}`; re-run will tag and release idempotently.\n"
            )
        with open(output_path, "a", encoding="utf-8") as f:
            f.write("bump_type=none\n")
            f.write(f"new_tag={existing_tag}\n")
        return

    try:
        last_tag = run("git describe --tags --abbrev=0")
        commits = run(f"git log {last_tag}..HEAD --pretty=format:%s").splitlines()
    except Exception:
        commits = run("git log --pretty=format:%s").splitlines()
        last_tag = "v0.0.0"

    commit_headers = commits
    commit_bodies = run(
        f"git log {last_tag}..HEAD --pretty=format:%B"
    )

    if any(BREAKING_HEADER_RE.match(h) for h in commit_headers) \
        or "BREAKING CHANGE:" in commit_bodies \
        or "BREAKING-CHANGE:" in commit_bodies:
        bump = "major"
    elif any(FEAT_RE.match(h) for h in commit_headers):
        bump = "minor"
    else:
        bump = "patch"

    current_version = get_current_version()
    new_version = bump_version(current_version, bump)

    with open(summary_path, "a", encoding="utf-8") as f:
        f.write(f"### Release Plan for {os.environ['GITHUB_REPOSITORY']}\n")
        f.write(
            f"* Detected Bump: `{bump.upper()}` | New Version: `v{new_version}`\n"
        )

    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"bump_type={bump}\n")
        f.write(f"new_tag=v{new_version}\n")


if __name__ == "__main__":
    main()
