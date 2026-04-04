#!/usr/bin/env python3
"""
fix_jsonld.py
Fix invalid JSON-LD structured data across all pages:
1. Double braces {{ -> { at start of JSON-LD
2. Multiple JSON objects in single script tag -> wrap in @graph or split
"""
import os, re, json, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"


def fix_jsonld_block(block):
    """Fix a single JSON-LD block."""
    block = block.strip()
    if not block:
        return block

    # Fix 1: Double opening braces {{ -> {
    if block.startswith('{{'):
        block = block[1:]  # Remove extra {
    if block.endswith('}}'):
        # Check if this is actually valid (nested objects can have }})
        # Only fix if the double }} is at the very end and doesn't match
        try:
            json.loads(block)
        except json.JSONDecodeError:
            block = block[:-1]  # Remove extra }

    # Fix 2: Multiple JSON objects concatenated
    # Pattern: } { or }\n{ between objects
    try:
        json.loads(block)
        return block  # Already valid
    except json.JSONDecodeError:
        pass

    # Try to split on }{ pattern (two JSON objects back to back)
    # Find the split point between two top-level objects
    parts = []
    depth = 0
    start = 0
    for i, ch in enumerate(block):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                part = block[start:i+1].strip()
                if part:
                    parts.append(part)
                start = i + 1

    if len(parts) > 1:
        # Multiple JSON objects - wrap in @graph
        valid_parts = []
        for part in parts:
            try:
                obj = json.loads(part)
                valid_parts.append(obj)
            except json.JSONDecodeError:
                # Try fixing double braces on this part too
                if part.startswith('{{'):
                    part = part[1:]
                if part.endswith('}}'):
                    part = part[:-1]
                try:
                    obj = json.loads(part)
                    valid_parts.append(obj)
                except json.JSONDecodeError:
                    continue

        if valid_parts:
            wrapper = {"@context": "https://schema.org", "@graph": valid_parts}
            return json.dumps(wrapper, ensure_ascii=False)

    # If nothing worked, try one more fix: remove trailing garbage
    try:
        json.loads(block)
        return block
    except json.JSONDecodeError:
        # Last resort: try to find valid JSON from start
        for end in range(len(block), 0, -1):
            try:
                json.loads(block[:end])
                return block[:end]
            except json.JSONDecodeError:
                continue

    return block


def fix_file(filepath):
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    original = html

    # Find all JSON-LD script blocks
    def replace_jsonld(match):
        block = match.group(1)
        fixed = fix_jsonld_block(block)
        return f'<script type="application/ld+json">\n    {fixed}\n    </script>'

    html = re.sub(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        replace_jsonld,
        html,
        flags=re.DOTALL
    )

    if html != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    total = 0
    updated = 0

    for root, dirs, files in os.walk(BASE):
        for f in files:
            if not f.endswith(".html"):
                continue
            filepath = os.path.join(root, f)
            total += 1
            if fix_file(filepath):
                updated += 1

    print(f"Done: {updated}/{total} files with JSON-LD fixed.")

    # Verify
    bad = 0
    for root, dirs, files in os.walk(BASE):
        for f in files:
            if not f.endswith(".html"):
                continue
            fp = os.path.join(root, f)
            with open(fp, encoding="utf-8", errors="ignore") as fh:
                html = fh.read()
            blocks = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.DOTALL)
            for block in blocks:
                block = block.strip()
                if not block:
                    continue
                try:
                    json.loads(block)
                except json.JSONDecodeError:
                    bad += 1
                    break

    print(f"Remaining files with invalid JSON-LD: {bad}")


if __name__ == "__main__":
    main()
