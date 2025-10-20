# app/main_gui.py  — PyQt5 (panel Options + styling digabung di sini)
from PyQt5 import QtWidgets, QtCore
from ui.ui_main_window import Ui_mainWindow
import ui.resources_rc                      # agar resource :/img/... terbaca
from .interface import wire_browse_handlers
from app.config import MASTER_SHEET_NAMES, DEFAULT_BARGE_SHEET


def create_window() -> QtWidgets.QDialog:
    dlg = QtWidgets.QDialog()
    ui = Ui_mainWindow()
    ui.setupUi(dlg)

    # --- Panel opsi di atas tombol Submit ---
    panel = QtWidgets.QGroupBox(dlg)
    panel.setObjectName("optionsPanel")
    panel.setGeometry(QtCore.QRect(329, 320, 420, 120))  # geser naik sedikit


    lay = QtWidgets.QGridLayout(panel)
    lay.setContentsMargins(12, 18, 12, 12)
    lay.setHorizontalSpacing(10)
    lay.setVerticalSpacing(8)

    # ====== STYLE supaya terbaca & konsisten ======
    panel.setStyleSheet("""
    QGroupBox#optionsPanel {
      background: rgba(0, 0, 0, 140);      /* panel semi-transparan */
      border: 1px solid rgba(255,255,255,60);
      border-radius: 12px;
    }
    QGroupBox#optionsPanel::title {
      subcontrol-origin: margin;
      left: 12px; top: -6px;
      padding: 0 6px;
      color: white;
      font: 600 10pt "Segoe UI";
    }
    QGroupBox#optionsPanel QLabel,
    QGroupBox#optionsPanel QCheckBox {
      color: white;
      font: 600 9pt "Segoe UI";
    }
    QGroupBox#optionsPanel QComboBox,
    QGroupBox#optionsPanel QSpinBox,
    QGroupBox#optionsPanel QLineEdit {
      background: rgba(255,255,255, 230);
      color: #1e1e1e;
      border: 1px solid #888;
      border-radius: 6px;
      padding: 2px 6px;
      min-height: 26px;
    }
    """)

    # Year
    ui.comboYear = QtWidgets.QComboBox(panel)
    for y in sorted(MASTER_SHEET_NAMES.keys()):
        ui.comboYear.addItem(str(y))
    ui.comboYear.setCurrentText(str(max(MASTER_SHEET_NAMES.keys())))
    lay.addWidget(QtWidgets.QLabel("Year:"), 0, 0)
    lay.addWidget(ui.comboYear, 0, 1)

    # Barge Sheet (akan diisi otomatis setelah pilih file barge)
    ui.comboSheet = QtWidgets.QComboBox(panel)
    ui.comboSheet.addItem(DEFAULT_BARGE_SHEET)
    lay.addWidget(QtWidgets.QLabel("Barge Sheet:"), 0, 2)
    lay.addWidget(ui.comboSheet, 0, 3)

    # Start Row & Row Count
    ui.spinStart = QtWidgets.QSpinBox(panel)
    ui.spinStart.setRange(1, 1_000_000)
    ui.spinStart.setValue(246)

    ui.spinCount = QtWidgets.QSpinBox(panel)
    ui.spinCount.setRange(0, 1_000_000)
    ui.spinCount.setValue(29)

    lay.addWidget(QtWidgets.QLabel("Start Row:"), 1, 0)
    lay.addWidget(ui.spinStart, 1, 1)
    lay.addWidget(QtWidgets.QLabel("Row Count:"), 1, 2)
    lay.addWidget(ui.spinCount, 1, 3)

    # # # Flags
    # # ui.chkCompleted = QtWidgets.QCheckBox("Only Completed", panel)
    # # ui.chkCompleted.setChecked(True)
    # ui.chkDryRun = QtWidgets.QCheckBox("Dry-run", panel)
    # ui.chkDryRun.setChecked(True)
    # # lay.addWidget(ui.chkCompleted, 2, 0, 1, 2)
    # lay.addWidget(ui.chkDryRun,    2, 2, 1, 2)

    # Sambungkan semua tombol/opsi dengan logic
    wire_browse_handlers(dlg, ui)

    return dlg
