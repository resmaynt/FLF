# ui/ui_main_window.py  -- PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Import resource yang robust (support run dari root atau dari folder ui)
try:
    from . import resources_rc   # saat di-import sebagai ui.ui_main_window
except Exception:                 # fallback jika dijalankan langsung dari folder ui
    import resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName("mainWindow")

        # Ukuran awal
        mainWindow.resize(1019, 632)

        # ---- Kunci ukuran & matikan maximize (PASTI di luar setStyleSheet) ----
        mainWindow.setFixedSize(1019, 632)                         # minimum = maximum
        mainWindow.setSizeGripEnabled(False)                       # hilangkan pegangan resize (QDialog)
        mainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # Opsional (efek terutama di Windows)
        mainWindow.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint, True)
        # ----------------------------------------------------------------------

        mainWindow.setStyleSheet(
            "#mainWindow {\n"
            "    border-image: url(:/img/2.jpg) 0 0 0 0 stretch stretch;\n"
            "}\n"
            "QWidget#mainWindow{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.274, y1:0.295, x2:1, y2:1,\n"
            "        stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
        )

        self.label = QtWidgets.QLabel(mainWindow)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(210, 20, 700, 91))
        self.label.setStyleSheet('font: 600 28pt "Segoe UI"; color: rgb(255, 255, 255);')

        self.label_2 = QtWidgets.QLabel(mainWindow)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(440, 120, 161, 31))
        font = QtGui.QFont("Segoe UI", 10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('color: rgb(255, 255, 255); font: 75 10pt "Segoe UI";')

        self.pushButton = QtWidgets.QPushButton(mainWindow)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(440, 460, 161, 41))
        self.pushButton.setFont(QtGui.QFont("Segoe UI", 9))
        self.pushButton.setStyleSheet(
            "QPushButton {"
            "  border-radius: 15px;"
            "  border: 1px solid transparent;"
            "  padding: 4px;"
            '  font: 600 9pt "Segoe UI";'
            "  color: rgb(255, 255, 255);"
            "  background-color: rgb(49, 99, 148);"
            "}"
            "QPushButton:pressed {"
            "  border-color: #888;"
            "  background-color: rgb(44, 88, 132);"
            "}"
        )

        self.pushButton_3 = QtWidgets.QPushButton(mainWindow)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(680, 250, 71, 41))
        self.pushButton_3.setStyleSheet(
            "QPushButton {"
            "  border-radius: 5px;"
            "  border: 1px solid transparent;"
            "  padding: 4px;"
            '  font: 600 8pt "Segoe UI";'
            "  color: rgb(255, 255, 255);"
            "  background-color: rgb(49, 99, 148);"
            "}"
            "QPushButton:pressed {"
            "  border-color: #888;"
            "  background-color: rgb(44, 88, 132);"
            "}"
        )

        self.fileLineEdit_2 = QtWidgets.QLineEdit(mainWindow)
        self.fileLineEdit_2.setObjectName("fileLineEdit_2")
        self.fileLineEdit_2.setGeometry(QtCore.QRect(340, 250, 331, 41))
        self.fileLineEdit_2.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        )
        self.fileLineEdit_2.setStyleSheet(
            "QLineEdit { border: 1px solid #888; border-radius: 4px; padding: 4px; }"
        )
        self.fileLineEdit_2.setPlaceholderText("Draft Power BI")
        self.fileLineEdit_2.setClearButtonEnabled(True)

        self.fileLineEdit = QtWidgets.QLineEdit(mainWindow)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.fileLineEdit.setGeometry(QtCore.QRect(340, 190, 331, 41))
        self.fileLineEdit.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        )
        self.fileLineEdit.setStyleSheet(
            "QLineEdit { border: 1px solid #888; border-radius: 4px; padding: 4px; }"
        )
        self.fileLineEdit.setPlaceholderText("FLF Report Data")
        f = QtGui.QFont("Segoe UI", 8)
        self.fileLineEdit.setFont(f)
        self.fileLineEdit_2.setFont(f)
        self.fileLineEdit.setClearButtonEnabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(mainWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(680, 190, 71, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton {"
            "  border-radius: 5px;"
            "  border: 1px solid transparent;"
            "  padding: 4px;"
            '  font: 600 8pt "Segoe UI";'
            "  color: rgb(255, 255, 255);"
            "  background-color: rgb(49, 99, 148);"
            "}"
            "QPushButton:pressed {"
            "  border-color: #888;"
            "  background-color: rgb(44, 88, 132);"
            "}"
        )
        self.pushButton_2.setCheckable(False)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _t = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_t("mainWindow", "Dialog"))
        self.label.setText(_t("mainWindow", "Complete the Required Data"))
        self.pushButton.setText(_t("mainWindow", "Submit"))
        self.pushButton_2.setText(_t("mainWindow", "browser"))
        self.pushButton_3.setText(_t("mainWindow", "browser"))
