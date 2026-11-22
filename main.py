#!/usr/bin/env python3
"""Entrypoint for the news-image-20261122 entry.

The front page was drawn ahead of time and checked in as entry.png
(1024x1024, 166,981 bytes). This program does the one job the harness
asks for: it places that exact file at $MAKEFUN_OUTPUT_DIR/entry.png
(/output by default). It uses only the standard library, touches no
network, and writes nothing anywhere else.

Before writing, it checks the file it ships: the first eight bytes
must be the PNG signature, and the file must be no larger than the
1 MiB the rules allow. After writing, it reads the copy back and
compares SHA-256 hashes, so a partial or altered write is caught
instead of silently graded. Any failure exits non-zero with the
reason on stderr.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def fail(message):
    print(f"entry: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    try:
        with open(SOURCE, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail(f"cannot read {SOURCE}: {exc}")

    if data[:8] != PNG_MAGIC:
        shown = data[:8].hex() if data else "(empty file)"
        fail(f"entry.png is not a PNG (first bytes: {shown})")
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} limit")

    digest = hashlib.sha256(data).hexdigest()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
        with open(target, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        fail(f"cannot write {target}: {exc}")

    if hashlib.sha256(written).hexdigest() != digest:
        fail("copy failed verification: hash mismatch after writing")
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
