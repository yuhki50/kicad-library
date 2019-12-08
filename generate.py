#!/usr/bin/env python

# require Python 3.8.0 or newer

from pathlib import Path

try:
    script_dir = Path(__file__).parent.resolve()

    with (script_dir / "sym-lib-table").open("w") as f:
        f.write("\n".join([
            "(sym_lib_table",
            "\n".join([
                f"""  (lib (name {v.stem})(type Legacy)(uri ${{KIPRJMOD}}/library/{v.name})(options "")(descr ""))"""
                for v in sorted(script_dir.glob("*.lib"), key=lambda v: v.stem)
            ]),
            ")",
        ]))

except KeyboardInterrupt:
    pass
