# run.py
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from app.main_gui_modern import create_window
import ui.resources_rc  
import os

def apply_theme(app, fname="theme.qss"):
    # load theme setelah resources diimport
    try:
        with open("theme.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print("Skip theme.qss:", e)

if __name__ == "__main__":
    # HiDPI
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QtGui.QFont("Segoe UI", 10, 600))  # 10pt, weight 600 (semi-bold)



    apply_theme(app, "theme.qss")

    win = create_window()
    win.setWindowTitle("FLF Automation System ")
    win.show()
    sys.exit(app.exec_())
