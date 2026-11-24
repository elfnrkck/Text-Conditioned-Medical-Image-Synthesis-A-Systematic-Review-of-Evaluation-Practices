"""Deduplication rule (Section 1.3 of the article).

Records are merged when they share a DOI, share a normalized title longer than 15 characters, or have normalized titles whose
difflib similarity ratio exceeds 0.93 (compared within buckets of the same first 12 characters). Merged groups are linked
transitively; the record from the highest-priority database (Scopus, then Web of Science, then PubMed) is kept and missing
abstracts and DOIs are filled from the other records of the group.
Usage: python deduplicate.py records.csv   (columns: database, id, title, doi, abstract)
"""
import csv, collections, difflib, re, sys, unicodedata

PRIORITY = {'Scopus': 0, 'WoS': 1, 'PubMed': 2}

def norm_title(t):
    t = unicodedata.normalize('NFKD', t or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]', '', t)

def deduplicate(records):
    R = sorted(records, key=lambda r: PRIORITY.get(r['database'], 9))
    for r in R:
        r['nt'] = norm_title(r['title'])
        d = re.sub(r'^https?://(dx\.)?doi\.org/', '', (r.get('doi') or '').strip().lower())
        r['doi'] = d if d.startswith('10.') else ''
    parent = list(range(len(R)))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    def union(i, j):
        a, b = find(i), find(j)
        if a != b: parent[max(a, b)] = min(a, b)
    keys = collections.defaultdict(list)
    for i, r in enumerate(R):
        if r['doi']: keys['d' + r['doi']].append(i)
        if len(r['nt']) > 15: keys['t' + r['nt']].append(i)
    for v in keys.values():
        for j in v[1:]: union(v[0], j)
    buckets = collections.defaultdict(list)
    for i, r in enumerate(R): buckets[r['nt'][:12]].append(i)
    for v in buckets.values():
        for a in range(len(v)):
            for b in range(a + 1, len(v)):
                if find(v[a]) != find(v[b]) and difflib.SequenceMatcher(None, R[v[a]]['nt'], R[v[b]]['nt']).ratio() > 0.93:
                    union(v[a], v[b])
    groups = collections.defaultdict(list)
    for i in range(len(R)): groups[find(i)].append(i)
    out = []
    for idx in groups.values():
        rec = dict(R[idx[0]]); rec['databases'] = '; '.join(sorted({R[i]['database'] for i in idx}, key=lambda d: PRIORITY.get(d, 9)))
        for fld in ('abstract', 'doi'):
            if not rec.get(fld): rec[fld] = next((R[i][fld] for i in idx if R[i].get(fld)), '')
        out.append(rec)
    return out

if __name__ == '__main__':
    with open(sys.argv[1], newline='', encoding='utf-8') as f:
        recs = list(csv.DictReader(f))
    u = deduplicate(recs)
    print('records', len(recs), 'unique', len(u), 'duplicates removed', len(recs) - len(u))
