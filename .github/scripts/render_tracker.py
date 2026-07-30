#!/usr/bin/env python3
"""Regenerate the accessibility-tracker PR tables from tracked_prs.json and
detect merged PRs by the tracked authors that are missing from the manifest.

- Tables live in README.md between `<!-- prs:<key>:start -->` / `<!-- prs:<key>:end -->`
  markers and are rendered purely from the manifest (no network needed, fully
  deterministic). Add a PR to the manifest to add a row.
- Detection queries the live GitHub API (via the `gh` CLI) for merged PRs by the
  primary authors in each repo and reports any that are not in the manifest, so
  the tracker can never silently fall behind.

Usage:
  python render_tracker.py            regenerate README + run detection
  python render_tracker.py --check    fail (exit 1) if README is out of date; still detects
"""
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]                      # repo root (…/.github/scripts/x.py -> root)
DATA = ROOT / ".github" / "data" / "tracked_prs.json"
README = ROOT / "README.md"


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def render_rows(section):
    base = f"https://github.com/{section['repo']}"
    lines = ["| PR | Title | Author | First Release |", "|---|---|---|---|"]
    for pr in section["prs"]:
        title = pr["title"].replace("|", "\\|")
        author = pr["author"]
        lines.append(
            f"| [#{pr['n']}]({base}/pull/{pr['n']}) | {title} | "
            f"[@{author}](https://github.com/{author}) | {pr['release']} |"
        )
    return "\n".join(lines)


def splice(readme, key, block):
    start, end = f"<!-- prs:{key}:start -->", f"<!-- prs:{key}:end -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(readme):
        raise SystemExit(f"error: markers for section '{key}' not found in README.md")
    return pattern.sub(lambda _m: f"{start}\n{block}\n{end}", readme)


def gh(args):
    """Run a gh command; return stdout on success, or None on any failure."""
    try:
        result = subprocess.run(
            ["gh", *args], capture_output=True, text=True, timeout=120
        )
    except Exception:
        return None
    return result.stdout if result.returncode == 0 else None


def detect(data):
    reports = []
    for section in data["sections"]:
        if not section.get("detect"):
            continue
        tracked = {pr["n"] for pr in section["prs"]}
        ignore = set(section.get("ignore", []))
        found = set()
        for author in data["primary_authors"]:
            # REST search API (reliable, unlike the GraphQL-backed `gh pr list`).
            out = gh([
                "api", "-X", "GET", "search/issues",
                "-f", f"q=repo:{section['repo']} author:{author} is:pr is:merged",
                "-f", "per_page=100", "--jq", ".items[].number",
            ])
            if out is None:
                reports.append(f"- ⚠️ could not query `{section['repo']}` "
                               f"(author `{author}`) — skipped this run")
                continue
            found.update(int(x) for x in out.split())
        for n in sorted(found - tracked - ignore):
            title = (gh(["api", f"repos/{section['repo']}/pulls/{n}",
                         "--jq", ".title"]) or "").strip()
            reports.append(
                f"- **[{section['repo']}#{n}](https://github.com/{section['repo']}/pull/{n})** "
                f"— {title}"
            )
    return reports


def emit_output(name, value):
    out_path = os.environ.get("GITHUB_OUTPUT")
    if out_path:
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(f"{name}={value}\n")


def main():
    check = "--check" in sys.argv
    data = load()
    readme = README.read_text(encoding="utf-8")

    updated = readme
    for section in data["sections"]:
        updated = splice(updated, section["key"], render_rows(section))
    changed = updated != readme

    if check:
        print("README tables are OUT OF DATE with the manifest." if changed
              else "README tables match the manifest.")
    elif changed:
        README.write_text(updated, encoding="utf-8")
        print("README tables regenerated.")
    else:
        print("README tables already up to date.")

    reports = detect(data)
    if reports:
        body = ("### Untracked merged PRs\n\n"
                "These merged PRs by the tracked authors are not yet in "
                "`.github/data/tracked_prs.json`:\n\n" + "\n".join(reports) + "\n")
    else:
        body = "All merged PRs by the tracked authors are present in the tracker. ✅\n"

    (ROOT / "tracker-report.md").write_text(body, encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(body)
    print("\n" + body)

    emit_output("changed", "true" if changed else "false")
    emit_output("has_new", "true" if reports else "false")

    if check and changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
