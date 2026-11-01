#!/usr/bin/env python3
"""front_matter.md + chapters/NN_final.md -> 04_manuscript.md (v1.0.0 조립 방식 그대로)."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent
chdir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'chapters'
front = (root / 'front_matter.md').read_text().rstrip()
chs = [p.read_text().strip() for p in sorted(chdir.glob('[0-9][0-9]_final.md'))]
out = front + '\n\n---\n\n\n' + '\n\n---\n\n\n'.join(chs) + '\n\n---\n\n'
dest = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / '04_manuscript.md'
dest.write_text(out)
print(f'wrote {dest} ({len(chs)} chapters, {len(out)} chars)')
