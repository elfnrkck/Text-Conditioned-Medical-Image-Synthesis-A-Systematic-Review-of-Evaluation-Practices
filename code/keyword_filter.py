"""Documented keyword filter (Section 1.3 of the article).

A record is retained for title and abstract screening if its title, abstract or keywords match either pattern:
STRONG, an explicit text-conditioned generation term, or GENERAL, a general image generation term.
Usage: python keyword_filter.py records.csv   (columns: id, title, abstract, keywords)
"""
import csv, re, sys

STRONG = re.compile(r"text[\s-]*to[\s-]*(image|medical|ct|mri|x[\s-]?ray|cxr|video|3d|volume|pathology|histopath)|report[\s-]*to[\s-]*(image|ct|x[\s-]?ray|cxr)|(text|report|prompt|language|caption|description|instruction)[\s-]*(guided|conditioned|conditional|driven|based|controlled|aware)\s+(\w+\s+){0,4}(generat|synthes|diffusion|editing)|(generat|synthes)\w*\s+(\w+\s+){0,6}(from|using|with|based on|conditioned on|guided by)\s+(\w+\s+){0,3}(text|report|prompt|caption|description|language)|dall[\s·\-]?e|midjourney|stable diffusion|imagen\b|firefly|text[\s-]*prompt|chatgpt[\s-]*4o?\s+image|gpt[\s-]*4o\s+image|image generator|ai[\s-]*generated (image|illustration|figure)|generative (ai|artificial intelligence)[^.]{0,60}(image|illustration|picture|visual)", re.I)
GENERAL = re.compile(r"(generat|synthes)\w*\W+(\w+\W+){0,4}(image|images|scan|scans|radiograph|volume|video|picture|illustration|figure)|(image|images|video|picture|illustration)\W+(\w+\W+){0,2}(generat|synthes)|synthetic (image|data|radiograph|scan)|diffusion model|generative (ai|artificial|model|adversarial)|text-to-image|dall|midjourney|stable diffusion|gpt-4o", re.I)

def retained(title, abstract, keywords):
    text = ' . '.join([title or '', abstract or '', keywords or ''])
    return bool(STRONG.search(text) or GENERAL.search(text))

if __name__ == '__main__':
    with open(sys.argv[1], newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            print(r['id'], 'retain' if retained(r.get('title'), r.get('abstract'), r.get('keywords')) else 'remove')
