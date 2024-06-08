import yaml
import json
import os, glob

def extract_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        text_between_dashes = []
        inside_dashes = False
        for line in lines:
            if line.strip() == '---':
                inside_dashes = not inside_dashes
            elif inside_dashes:
                text_between_dashes.append(line.strip())
        print(text_between_dashes)
        return '\n'.join(text_between_dashes)
    
for file in glob.glob('*.md'):
    extract_frontmatter(file)
