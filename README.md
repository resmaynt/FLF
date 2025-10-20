
# Barge → Master Excel Automation (Qt + Pandas + OpenPyXL)

A small desktop tool to take rows from **Barge Line Up 2025** and post totals into **master 2** (sheets 2023/2024/2025) by month and FLF (Apollo, Zeus, Mara, August, Eagle, WHS, Bulk Java, Ratu Dewata, Labor, Green Calypso).

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/main_gui.py
```

## Typical workflow
1) Open **Qt Designer** (optional) and tweak `ui/main_window.ui`.
2) (Optional) Convert `.ui` → `.py`:  
   `python tools/convert_ui.py`  (uses the `pyside6-uic` command if available)
3) Run the app: `python app/main_gui.py`
4) In the UI, pick:
   - *Master workbook*: `master 2.xlsx`
   - *Barge workbook*: `Barge Line Up 2025.xlsx`
   - Choose target **Year** (2023/2024/2025), Barge sheet (default: `VLU 2025`).
   - Input *Start row* and *Row count* (example from screenshot: `246` and `28`).
   - Keep *Only STATUS = COMPLETED* checked (recommended).
5) Click **Run**. The tool will sum ACTUAL LOADED by FLF/FC NOMINATE per month,
   then **add** those totals into the corresponding month row in the master sheet
   (summing with any existing numbers).

## Matching rules
- Exact match between `FLF/FC NOMINATE` and the master FLF columns is used first.
- You can customize synonyms/splitting in `mapping.py` (e.g., `"WHS ISKANDAR" -> "WHS"`, `"ZEUS-APOLLO" -> ["ZEUS","APOLLO"]`).  
- Configure columns or behaviors in `config.py`.

## Files
- `app/main_gui.py` — App entry.
- `app/interface.py` — Wire UI <-> logic, file browsing, logging.
- `app/main_logic.py` — Excel parsing and update logic.
- `app/mapping.py` — Canonicalization & synonyms for FLF names.
- `app/config.py` — Central configuration (sheets, columns).
- `ui/main_window.ui` — Qt Designer UI.
- `tools/convert_ui.py` — Optional `.ui` → `.py` generator.
- `requirements.txt` — Dependencies.

> Tip: Work on a copy of your workbooks. The app writes back to `master 2.xlsx`.
