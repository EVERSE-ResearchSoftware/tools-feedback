# 📤 Exporting Issues

Use the script below to export repository issues as one YAML file per issue.

```bash
python3 scripts/export_issues.py --output-dir data/issues
```

Notes:

* Requires the GitHub CLI (`gh`) with an authenticated session.
* By default exports open issues only and excludes pull requests.
* Use `--state all` or `--include-prs` to adjust the scope.