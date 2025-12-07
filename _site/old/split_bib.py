import re

def split_bib_file(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = re.split(r'(?=@)', content)
    
    for entry in entries:
        if entry.strip():
            match = re.search(r'@\w+{\s*(\w+)', entry)
            if match:
                citekey = match.group(1)
                output_file = f"{output_dir}/{citekey}.bib"
                with open(output_file, 'w') as f:
                    f.write(entry.strip())

# Usage
split_bib_file('articles.bib', '../bib')
