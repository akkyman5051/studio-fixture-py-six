"""Item 09 live-run fixture (8.3, V26): uses the installed six wheel and writes its result to /work/out/."""
import os

import six

os.makedirs("/work/out/", exist_ok=True)
with open("/work/out/result.txt", "w", encoding="utf-8") as handle:
    handle.write("six %s %s\n" % (six.__version__, six.ensure_str(b"used")))
