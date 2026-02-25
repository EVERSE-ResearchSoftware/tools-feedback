#!/usr/bin/env python3
"""
Export GitHub issues to Markdown files using the GitHub CLI.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from typing import Iterable


def detect_repo() -> str | None:
    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        check=False,
        capture_output=True,
        text=True,
    )
    remote = result.stdout.strip()
    if not remote:
        return os.environ.get("GITHUB_REPOSITORY")

    # Supports HTTPS and SSH URLs
    match = re.search(r"github.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)", remote)
    if not match:
        return None
    return f"{match.group('owner')}/{match.group('repo')}"


def slugify(text: str, max_length: int = 60) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    if not cleaned:
        cleaned = "issue"
    return cleaned[:max_length].strip("-")


def fetch_issues(repo: str, state: str) -> list[dict]:
    command = [
        "gh",
        "api",
        "-X",
        "GET",
        "--paginate",
        f"/repos/{repo}/issues",
        "-f",
        f"state={state}",
        "-f",
        "per_page=100",
        "--jq",
        ".[]",
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(message or "Failed to fetch issues via gh")

    issues: list[dict] = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line:
            issues.append(json.loads(line))
    return issues


def yaml_escape(text: str) -> str:
    needs_quotes = (
        any(ch in text for ch in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "-", "@", "`", '"', "'", "\n"])
        or text.strip() != text
    )
    if not needs_quotes:
        return text
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def format_issue_yaml(issue: dict, exported_at: str) -> str:
    labels = [label["name"] for label in issue.get("labels", [])]
    body = issue.get("body") or ""
    body = body.replace("\r\n", "\n").rstrip()

    lines = [
        f"number: {issue.get('number', '')}",
        f"title: {yaml_escape(issue.get('title', 'Untitled'))}",
        f"state: {yaml_escape(issue.get('state', 'unknown'))}",
        f"author: {yaml_escape(issue.get('user', {}).get('login', 'unknown'))}",
        "labels:",
    ]
    if labels:
        for label in labels:
            lines.append(f"  - {yaml_escape(label)}")
    else:
        lines.append("  -")

    lines.extend(
        [
            f"created: {yaml_escape(issue.get('created_at', 'unknown'))}",
            f"updated: {yaml_escape(issue.get('updated_at', 'unknown'))}",
            f"exported: {yaml_escape(exported_at)}",
            f"url: {yaml_escape(issue.get('html_url', ''))}",
            "body: |",
        ]
    )
    if body:
        for line in body.split("\n"):
            lines.append(f"  {line}")
    else:
        lines.append("  ")

    return "\n".join(lines) + "\n"


def write_issues(issues: Iterable[dict], output_dir: str, exported_at: str) -> int:
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for issue in issues:
        number = issue.get("number")
        title = issue.get("title") or "issue"
        filename = f"{number:05d}-{slugify(title)}.yml"
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(format_issue_yaml(issue, exported_at))
        count += 1
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export GitHub issues to Markdown files using gh.",
    )
    parser.add_argument(
        "--repo",
        help="Repository in owner/name format. Defaults to git remote origin.",
    )
    parser.add_argument(
        "--state",
        choices=["open", "closed", "all"],
        default="open",
        help="Issue state to export.",
    )
    parser.add_argument(
        "--include-prs",
        action="store_true",
        help="Include pull requests (issues only by default).",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join("data", "issues"),
        help="Directory to write Markdown files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo = args.repo or detect_repo()
    if not repo:
        raise SystemExit("Could not detect repo. Pass --repo owner/name.")

    issues = fetch_issues(repo, args.state)
    if not args.include_prs:
        issues = [issue for issue in issues if "pull_request" not in issue]

    exported_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    count = write_issues(issues, args.output_dir, exported_at)
    print(f"Wrote {count} issue file(s) to {args.output_dir}")


if __name__ == "__main__":
    main()
