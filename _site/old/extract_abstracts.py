import bibtexparser
import os

def extract_abstracts(bib_file, output_dir):
    with open(bib_file, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    for entry in bib_database.entries:
        if 'abstract' in entry and 'ID' in entry:
            abstract = entry['abstract']
            citation_key = entry['ID']
            
            output_file = os.path.join(output_dir, f"{citation_key}.html")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(abstract)

# Usage
extract_abstracts('articles.bib', '../abstract')
