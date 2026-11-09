#!/usr/bin/env python3
"""Sanity checks for the static site (standard library only).

    python3 tools/check_site.py            # errors fail, placeholders only warn
    python3 tools/check_site.py --strict   # run this before publishing

Checks index.html for: missing local files, #anchors without a matching id,
images without alt text, external links that open a new tab without
rel="noopener", duplicate ids, and leftover [PLACEHOLDER] text.
"""

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _-]{2,}\]")


class PageScanner(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.anchors = []      # (href, line)
        self.local_files = []  # (path, line)
        self.errors = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        line = self.getpos()[0]

        if attrs.get("id"):
            self.ids.append(attrs["id"])

        href = attrs.get("href") or ""
        src = attrs.get("src") or ""

        if tag == "a" and href.startswith("#"):
            self.anchors.append((href[1:], line))
        for target in (href, src):
            if target and not re.match(r"^(https?:|mailto:|tel:|data:|#|//)", target):
                self.local_files.append((target.split("#")[0].split("?")[0], line))

        if tag == "img" and "alt" not in attrs:
            self.errors.append(f"line {line}: <img src=\"{src}\"> has no alt attribute")
        if tag == "a" and attrs.get("target") == "_blank":
            rel = (attrs.get("rel") or "").split()
            if "noopener" not in rel and "noreferrer" not in rel:
                self.errors.append(f"line {line}: link to {href} opens a new tab without rel=\"noopener\"")

    def handle_data(self, data):
        self.text.append(data)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true", help="treat leftover placeholders as errors")
    args = parser.parse_args(argv)

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    scanner = PageScanner()
    scanner.feed(html)

    errors = list(scanner.errors)
    warnings = []

    duplicates = sorted({i for i in scanner.ids if scanner.ids.count(i) > 1})
    for dup in duplicates:
        errors.append(f"duplicate id \"{dup}\"")
    for anchor, line in scanner.anchors:
        if anchor and anchor not in scanner.ids:
            errors.append(f"line {line}: link to #{anchor} but no element has that id")
    for path, line in scanner.local_files:
        if path and not (ROOT / path).exists():
            errors.append(f"line {line}: file \"{path}\" does not exist")

    for match in sorted(set(PLACEHOLDER.findall("".join(scanner.text)))):
        message = f"placeholder text still on the page: {match}"
        (errors if args.strict else warnings).append(message)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("OK: no errors" + (f" ({len(warnings)} warning(s))" if warnings else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
