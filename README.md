# FLF Automation System

A desktop application built with **PyQt5** for automating FLF data integration between “Barge Report” and “Master Power BI” Excel workbooks.

This tool is designed to streamline monthly data consolidation and ensure consistency across FLF datasets.

## Environment

Requires **Python ≥ 3.10** (due to use of modern type hints

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Workflow

---

1. Select **FLF Report (Barge)** and **Final (Master)** Excel files.
2. Choose target year, sheet, starting row, and number of rows.
3. Confirm data summary.
4. Process:
   * Reads Barge sheet (detects header)
   * Filters *Status = Complete*
   * Aggregates totals per FLF per month
   * Writes to Master workbook
5. View detailed logs in the UI.
6. Click **End** to reset state.

---

## Features

✅ Modern PyQt5 GUI (with sidebar navigation)

✅ Excel data parsing using **pandas + openpyxl**

✅ Dynamic sheet & row detection

✅ “Clear row before write” option to avoid data duplication

✅ Live log window & progress reporting

✅ Reloads runtime modules to reset state after each r

## Matching rules

- Exact match between `FLF/FC NOMINATE` and the master FLF columns is used first.
- You can customize synonyms/splitting in `mapping.py` (e.g., `"WHS ISKANDAR" -> "WHS"`, `"ZEUS-APOLLO" -> ["ZEUS","APOLLO"]`).
- Configure columns or behaviors in `config.py`.

## Files

FLF-Automation/
│
├── app/
│   ├── main_gui_modern.py     # GUI logic (PyQt5 modern layout)
│   ├── main_logic.py          # Data processing pipeline
│   ├── config.py              # Configuration (sheet names, columns, etc.)
│   ├── mapping.py             # FLF name normalization/mapping
│   └── popup.py               # Confirmation popup dialog
│
├── ui/
│   ├── resources_rc.py        # Auto-generated from resources.qrc
│   └── resources.qrc          # Qt resources (images/icons)
│
├── theme.qss                  # Application stylesheet (dark theme)
├── run.py                     # Entry point to launch GUI
├── requirements.txt           # Python dependencies
└── README.md                  # This file

# Windows

.venv\Scripts\activate

# macOS / Linux

source .venv/bin/activate
pip install -r requirements.txt
python run.py

> Tip: Work on a copy of your workbooks. The app writes back to `master 2.xlsx`.
