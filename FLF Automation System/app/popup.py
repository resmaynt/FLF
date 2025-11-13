# app/popup.py
from PyQt5 import QtWidgets, QtCore, QtGui
# Contoh: pyrcc5 resources.qrc -o ui/resources_rc.py
import ui.resources_rc  # noqa: F401
from PyQt5 import QtWidgets, QtCore, QtGui



class DataConfirmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, text: str = "",
                 window_icon_path: str = ":/img/logo-side.jpg"):
        super().__init__(parent)
        self.setObjectName("ConfirmDialog")

        # SET IKON SEKALI, TANPA CEK QFile.exists (karena ini resource)
        self.setWindowIcon(QtGui.QIcon(window_icon_path))

        # === Tambahan: hilangkan '?' dan tampilkan tombol minimize di popup
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(QtCore.Qt.WindowSystemMenuHint, True)
        # (opsional) tombol maximize
        # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)


        # ukuran & judul
        self.resize(480, 400)
        self.setMinimumSize(QtCore.QSize(480, 400))
        self.setMaximumSize(QtCore.QSize(480, 400))
        self.setWindowTitle("Data Confirmation")
        self.setModal(True)

        # ===== Judul =====
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("titleLabel")
        self.label.setGeometry(QtCore.QRect(30, 20, 421, 21))
        self.label.setText("Please check if the data is correct?")

        # ===== Panel =====
        self.panel = QtWidgets.QFrame(self)
        self.panel.setObjectName("panel")
        self.panel.setGeometry(QtCore.QRect(20, 60, 441, 275))

        # ===== TextArea =====
        self.textEdit_popup = QtWidgets.QPlainTextEdit(self.panel)
        self.textEdit_popup.setObjectName("textEdit_popup")
        self.textEdit_popup.setGeometry(QtCore.QRect(10, 10, 421, 255))
        self.textEdit_popup.setReadOnly(True)
        self.textEdit_popup.setPlainText(text)
        self.textEdit_popup.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)

        # ===== Tombol =====
        self.btn_cancel = QtWidgets.QPushButton(self)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setGeometry(QtCore.QRect(120, 350, 120, 36))
        self.btn_cancel.setText("Cancel")
        self.btn_cancel.clicked.connect(self.reject)

        self.btn_ok = QtWidgets.QPushButton(self)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setGeometry(QtCore.QRect(260, 350, 120, 36))
        self.btn_ok.setText("OK")
        self.btn_ok.clicked.connect(self.accept)
        self.btn_ok.setDefault(True)
        self.btn_ok.setAutoDefault(True)

        # (styles kamu boleh tetap seperti semula)
        # self.setStyleSheet(""" ... """)

def confirm_summary(parent: QtWidgets.QWidget, text: str,
                    icon_path: str = ":/img/logo-side.jpg") -> bool:
    app = QtWidgets.QApplication.instance()
    old_font = app.font()
    normal = QtGui.QFont(old_font); normal.setBold(False); normal.setPointSize(10)
    app.setFont(normal)
    try:
        dlg = DataConfirmDialog(parent=parent, text=text, window_icon_path=icon_path)
        return dlg.exec_() == QtWidgets.QDialog.Accepted
    finally:
        app.setFont(old_font)

