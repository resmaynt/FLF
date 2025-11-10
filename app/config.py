from dataclasses import dataclass


# Kolom di master (sheet 2023/2024/2025)
MASTER_COLUMNS = {
    "Month/Year": "B",
    "Apollo": "C",
    "Zeus": "D",
    "Mara": "E",
    "August": "F",
    "Eagle": "G",
    "WHS": "H",
    "Bulk Java": "I",
    "Ratu Dewata": "J",
    "Labor": "K",
    "Green Calypso": "L",
    "FC Sumber":"M",
}

# Format teks bulan di master (mis. "Aug-25")
MASTER_MONTH_FORMAT = "%b-%y"

# Pemetaan 3 huruf bulan -> nomor
MONTH_NAME_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
}

BARGE_COLUMNS = {
    "No": "B",
    "Month": "C",
    "Status": "P",
    "ActualLoaded": "BN",
    "LoadingFacilities": "BP",
    "FLFNominate": "BQ",
}


# Mode gabungan FLF: "split"=bagi rata, "first"=ambil pertama, "dup"=duplikasi penuh
COMPOUND_FLF_MODE = "split"

# Paksa seluruh blok (start_row..start_row+row_count-1) ikut bulan header (baris pertama di blok)
FORCE_MONTH_FROM_HEADER = True

# Nama sheet master per tahun (harus sesuai tab di master 2.xlsx)
MASTER_SHEET_NAMES = {
    2023: "2023",
    2024: "2024",
    2025: "2025",
}

# Default nama sheet di workbook Barge
DEFAULT_BARGE_SHEET = "VLU 2025"

@dataclass
class RunOptions:
    master_path: str
    barge_path: str
    barge_sheet: str
    target_year: int
    start_row: int
    row_count: int
    only_completed: bool = False
    dry_run: bool = False
    clear_before_write: bool = True

def fmt_money(val: float) -> str:
    return f"{float(val):,.0f}"


