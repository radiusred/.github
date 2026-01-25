#!/usr/bin/env python3

import subprocess
import os
import re

BREAKING_HEADER_RE = re.compile(r"^[a-z]+(\([^)]+\))?!:")
FEAT_RE = re.compile(r"^feat(\([^)]+\))?:", re.IGNORECASE)


def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True).strip()


def main() -> None:
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

    run(f"hatch version {bump}")
    new_version = run("hatch version")

    summary_path = os.environ["GITHUB_STEP_SUMMARY"]
    output_path = os.environ["GITHUB_OUTPUT"]

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
