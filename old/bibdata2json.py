import re, json, sys

json_struct = []
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for entry in re.split(r'(?=@)', f.read()):
        if entry.strip():
            match = re.search(r'@\w+{\s*(\w+)', entry)
            if match:
                citekey = match.group(1)
                json_struct.append({"ID": citekey+"bib", "text": entry.strip()})

with open(sys.argv[2], 'w', encoding='utf-8') as jsonfile:
  json.dump(json_struct, jsonfile, indent=2, ensure_ascii=True)
