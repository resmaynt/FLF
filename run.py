# run.py
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from app.main_gui_modern import create_window
import ui.resources_rc  # penting agar resource ter-register

def apply_theme(app):
    try:
        f = QtCore.QFile(':/qss/theme.qss')
        if f.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            app.setStyleSheet(bytes(f.readAll()).decode('utf-8'))
        else:
            print("Skip theme.qss: cannot open from resource")
    except Exception as e:
        print("Skip theme.qss:", e)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QtGui.QFont("Segoe UI", 10))

    apply_theme(app)  # ← cukup panggil ini, tanpa path file

    win = create_window()
    win.setWindowTitle("FLF Automation System ")
    win.show()
    sys.exit(app.exec_())
