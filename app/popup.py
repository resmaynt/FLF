# app/popup.py
from PyQt5 import QtWidgets, QtCore, QtGui


class DataConfirmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, text: str = "",
                 window_icon_path: str = "assets/Coal_Supply_Chain.png"):
        super().__init__(parent)
        self.setObjectName("ConfirmDialog")

        # ukuran & judul
        self.resize(480, 400)
        self.setMinimumSize(QtCore.QSize(480, 400))
        self.setMaximumSize(QtCore.QSize(480, 400))
        self.setWindowTitle("Data Confirmation")
        self.setModal(True)

        # icon
        if window_icon_path and QtCore.QFile.exists(window_icon_path):
            icon = QtGui.QIcon(window_icon_path)
        else:
            icon = QtGui.QIcon(":/img/logo")
        self.setWindowIcon(icon)

        # ===== Judul =====
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("titleLabel")
        self.label.setGeometry(QtCore.QRect(30, 20, 421, 21))
        self.label.setText("Please check if the data is correct?")

        # ===== Panel =====
        self.panel = QtWidgets.QFrame(self)
        self.panel.setObjectName("panel")
        self.panel.setGeometry(QtCore.QRect(20, 60, 441, 275))
        
        # ===== TextArea (QPlainTextEdit) =====
        self.textEdit_popup = QtWidgets.QPlainTextEdit(self.panel)
        self.textEdit_popup.setObjectName("textEdit_popup")
        self.textEdit_popup.setGeometry(QtCore.QRect(10, 10, 421, 255))
        self.textEdit_popup.setReadOnly(True)
        self.textEdit_popup.setPlainText(text)
        self.textEdit_popup.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)

        # 1) FONT: non-bold + ukuran tetap (pixel) supaya tidak “terlihat nge-zoom”
        f = QtGui.QFont("Consolas")                 # monospace rapi untuk kolom-kolom
        f.setStyleHint(QtGui.QFont.Monospace)
        f.setFixedPitch(True)
        f.setBold(False)
        f.setWeight(QtGui.QFont.Normal)
        f.setPixelSize(13)                           # ≈ 10–11pt; kecil & jelas
        self.textEdit_popup.setFont(f)

        # 2) PAKSA normal secara CSS (kalau ada theme agresif)
        self.textEdit_popup.setStyleSheet(
            "font-family: Consolas; font-weight: 400 !important; font-size: 13px;"
        )

        # 3) RESET ZOOM internal editor (kalau sebelumnya sempat diperbesar)
        #    Dorong jauh ke kecil, lalu naikkan ke level nyaman -> netral
        self.textEdit_popup.zoomOut(50)
        self.textEdit_popup.zoomIn(5)

        # 4) (Opsional) Cegah Ctrl+Scroll mengubah zoom lagi
        def _wheel_event(e: QtGui.QWheelEvent):
            if e.modifiers() & QtCore.Qt.ControlModifier:
                e.ignore()  # blokir zoom
                return
            QtWidgets.QPlainTextEdit.wheelEvent(self.textEdit_popup, e)

        self.textEdit_popup.wheelEvent = _wheel_event

        # Font isi — NORMAL (tidak bold)
        font_normal = QtGui.QFont("Arial", 11)
        font_normal.setBold(False)
        font_normal.setWeight(QtGui.QFont.Normal)
        self.textEdit_popup.setFont(font_normal)

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

        # ===== Style =====
        self.setStyleSheet("""
        QDialog#ConfirmDialog { background: #0b0b0b; }

        QLabel#titleLabel {
            font-family: Arial;
            font-size: 15pt;
            font-weight: 700;
            color: #e5e7eb;
        }

        QFrame#panel {
            background: #111827;
            border: 1px solid #374151;
            border-radius: 10px;
        }

        QPlainTextEdit#textEdit_popup {
            background: #0f172a;
            border: 1px solid #374151;
            border-radius: 8px;
            padding: 6px;
            color: #e5e7eb;
            font-family: Arial;
            font-size: 11pt;
            font-weight: 400 !important;   /* 400 = normal, tidak bold */
        }

        QPushButton#btn_cancel, QPushButton#btn_ok {
            min-width: 120px;
            min-height: 36px;
            border-radius: 10px;
            background: #374151;
            color: #ffffff;
            border: 1px solid #2563eb;
            font-weight: 600;   /* tombol tetap tebal */
        }
        QPushButton#btn_cancel:hover, QPushButton#btn_ok:hover   { background: #4b5563; }
        QPushButton#btn_cancel:pressed, QPushButton#btn_ok:pressed { background: #111827; }
        QPushButton#btn_cancel:disabled, QPushButton#btn_ok:disabled {
            background: #9ca3af; color: #f3f4f6;
        }
        """)


def confirm_summary(parent: QtWidgets.QWidget, text: str,
                    icon_path: str = "assets/Coal_Supply_Chain.png") -> bool:
    app = QtWidgets.QApplication.instance()

    # 1) Simpan font global lama (yang semi-bold)
    old_font = app.font()

    # 2) Set sementara ke NORMAL + ukuran lebih kecil (biar tidak "nge-zoom")
    normal = QtGui.QFont(old_font)
    normal.setBold(False)
    normal.setWeight(QtGui.QFont.Normal)
    # pakai 10pt agar tidak terlihat besar; sesuaikan kalau mau lebih kecil
    normal.setPointSize(10)
    app.setFont(normal)

    try:
        dlg = DataConfirmDialog(parent=parent, text=text, window_icon_path=icon_path)

        # Paksa isi popup benar-benar normal (backup kalau theme.qss agresif)
        f = QtGui.QFont("Consolas", 10)  # monospace, jelas tidak bold
        f.setBold(False)
        f.setWeight(QtGui.QFont.Normal)
        dlg.textEdit_popup.setFont(f)
        dlg.textEdit_popup.setStyleSheet(
            "font-family: Consolas; font-size: 10pt; font-weight: 400 !important;"
        )

        return dlg.exec_() == QtWidgets.QDialog.Accepted
    finally:
        # 3) Kembalikan font global ke semula (supaya tombol2 di window utama tetap bold)
        app.setFont(old_font)
