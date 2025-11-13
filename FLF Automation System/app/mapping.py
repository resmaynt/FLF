import re
from typing import List

MASTER_KEYS = [
    "Apollo","Zeus","Mara","August","Eagle","WHS","Bulk Java","Ratu Dewata","Labor","Green Calypso", "FC Sumber"
]

# Variasi nama umum -> target
SYNONYMS_RAW = {
    "WHS ISKANDAR": "WHS",
    "WHS-ISKANDAR": "WHS",
    "WHS/ISKANDAR": "WHS",
    "WHSISKANDAR": "WHS",

    "ZEUS-APOLLO": ["Zeus","Apollo"],
    "ZEUS/APOLLO": ["Zeus","Apollo"],
    "APOLLO-ZEUS": ["Zeus","Apollo"],
    "APOLLO/ZEUS": ["Zeus","Apollo"],
    "ZEUSAPOLLO": ["Zeus","Apollo"],
    "APOLLOZEUS": ["Zeus","Apollo"],

    "BULKJAVA": "Bulk Java",
    "RATUDEWATA": "Ratu Dewata",
    "GREENCALYPSO": "Green Calypso",
    "MUTIARA JAWA": "Eagle",

    "FC SUMBER": "FC Sumber",
    "FC-SUMBER": "FC Sumber",
    "FCSUMBER": "FC Sumber",
    "FC SUMBER 1001": "FC Sumber",
    "FC-SUMBER-1001": "FC Sumber",
    "FCSUMBER1001": "FC Sumber",
}

def normalize_token(s: str) -> str:
    return re.sub(r"[^A-Z]", "", s.upper())

SYNONYMS = { normalize_token(k): v for k, v in SYNONYMS_RAW.items() }

def canonicalize(raw: str) -> List[str]:
    if not raw:
        return []
    token = normalize_token(raw)

    # via synonyms
    if token in SYNONYMS:
        v = SYNONYMS[token]
        return v if isinstance(v, list) else [v]

    # fallback: substring terhadap master keys
    matches = []
    for k in MASTER_KEYS:
        if normalize_token(k) in token:
            matches.append(k)

    # buang duplikat, pertahankan urutan
    seen, uniq = set(), []
    for m in matches:
        if m not in seen:
            uniq.append(m); seen.add(m)
    return uniq
