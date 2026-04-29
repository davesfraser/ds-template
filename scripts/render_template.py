from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/render_template.py <copier-source> <rendered-dir>")
        return 2

    copier_source = Path(sys.argv[1]).resolve()
    rendered = Path(sys.argv[2])
    subprocess.run(
        [
            sys.executable,
            "-m",
            "copier",
            "copy",
            str(copier_source),
            str(rendered),
            "--defaults",
            "--overwrite",
            "--quiet",
        ],
        check=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
