import bibtexparser
import json, sys
from unidecode import unidecode

# year and month sorting

month_map = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def year_month_key(entry):
    # Extract year as int; use 0 if missing/non-numeric for correct sorting
    year = int(entry.get('year', 0)) if entry.get('year', '').isdigit() else 0
    # Extract month as numeric using map; default to 0 if absent/invalid
    month_str = entry.get('month', '').lower()
    month = month_map.get(month_str, 0) 
    return (year, month)

# read .bib
with open(sys.argv[1], 'r', encoding='utf-8') as bibfile:
  bib_database = bibtexparser.load(bibfile)

# Sort entries descending by year and month
entries = sorted(
    bib_database.entries,
    key=year_month_key,
    reverse=True
)

# fix \n and "and" author list
for e in entries:
  for key, value in e.items():
    if isinstance(value, str):
      e[key] = value.replace("\n", " ")
      if key == "author": e[key] = value.replace(" and ", ", ")

# write json
with open(sys.argv[2], 'w', encoding='utf-8') as jsonfile:
  json.dump(entries, jsonfile, indent=2, ensure_ascii=True)
