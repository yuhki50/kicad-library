#!/usr/bin/env python

# require Python 3.8.0 or newer

from pathlib import Path

try:
    script_dir = Path(__file__).parent.resolve()

    with (script_dir / "sym-lib-table").open("w", newline="\n") as f:
        f.write("\n".join([
            "(sym_lib_table",
            "\n".join([
                f"""  (lib (name {v.stem})(type KiCad)(uri ${{KIPRJMOD}}/library/{v.name})(options "")(descr ""))"""
                for v in sorted(script_dir.glob("*.kicad_sym"), key=lambda v: v.stem)
            ]),
            ")",
        ]))

except KeyboardInterrupt:
    pass
