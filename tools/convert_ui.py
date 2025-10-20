"""
Optional helper to convert .ui → Python class using the external `pyside6-uic` tool.
Usage:
    python tools/convert_ui.py
This will create ui/ui_main_window.py from ui/main_window.ui (if `pyside6-uic` is installed).
"""
import subprocess
from pathlib import Path


root = Path(__file__).resolve().parents[1]
ui_src = root / "ui" / "mainWindow.ui"
ui_out = root / "ui" / "ui_main_window.py"

cmd = ["pyuic5", str(ui_src), "-o", str(ui_out)]
print("Running:", " ".join(cmd))
try:
    subprocess.check_call(cmd)
    print("OK ->", ui_out)
except FileNotFoundError:
    print("ERROR: `pyside6-uic` not found. Install PySide6 and ensure scripts are on PATH.")
except subprocess.CalledProcessError as e:
    print("uic failed:", e)
