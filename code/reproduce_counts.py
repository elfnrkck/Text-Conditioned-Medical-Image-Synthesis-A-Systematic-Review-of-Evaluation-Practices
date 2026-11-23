"""Reproduce the counts reported in the article from the study-level matrix and the screening log.

Run from the repository root:  python code/reproduce_counts.py
Requires Python 3.8+ and openpyxl (for the inter-rater agreement, read from screening/screening_log.xlsx).
"""
import csv, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, 'data', 'included_studies_generative.csv'), encoding='utf-8') as f:
    G = list(csv.DictReader(f))
with open(os.path.join(ROOT, 'data', 'included_studies_general_purpose.csv'), encoding='utf-8') as f:
    E = list(csv.DictReader(f))
CODES = [('F', 'F_fidelity'), ('A', 'A_alignment'), ('R', 'R_reader_study'), ('U', 'U_utility'), ('S', 'S_subgroup')]
def has(s, c): return s[dict(CODES)[c]] == 'reported'
def pct(a, b): return '%d (%.1f%%)' % (a, 100.0 * a / b)

print('Included studies: %d generative (G), %d evaluations of general-purpose generators (E)' % (len(G), len(E)))
print('\nYear (reference-list year):', dict(sorted(collections.Counter(s['year'] for s in G).items())))
print('Studies from 2024 onwards:', sum(int(s['year']) >= 2024 for s in G))

# ---------------- Table 3: by imaging domain
DOMAINS = ['Chest radiograph', 'CT', 'MRI', 'Histopathology and cytology', 'Dermatology', 'Endoscopy and surgical video', 'Ophthalmology',
           'Ultrasound', 'Other or not stated', 'Multiple domains']
print('\nTable 3  domain | n | 2D / 2D+t / 3D | free / structured / text + other | F | A | R | U')
def row(sub):
    d = collections.Counter(s['dimensionality'] for s in sub)
    c = collections.Counter(s['conditioning_axis'] for s in sub)
    other = len(sub) - c['Free-text report or description'] - c['Structured, templated or generated text']
    return '%d | %d / %d / %d | %d / %d / %d | %s' % (
        len(sub), d['2D'], d['2D+t'], d['3D'], c['Free-text report or description'], c['Structured, templated or generated text'], other,
        ' | '.join(str(sum(has(s, k) for s in sub)) for k in 'FARU'))
for dm in DOMAINS:
    print('  %-30s %s' % (dm, row([s for s in G if s['modality_group'] == dm])))
print('  %-30s %s' % ('All domains', row(G)))

# ---------------- Table 4: taxonomy axes
print('\nTable 4')
for ax in ['conditioning_axis', 'dimensionality', 'modality_group', 'adaptation', 'intended_use']:
    print('  %s: %s' % (ax, dict(collections.Counter(s[ax] for s in G).most_common())))

# ---------------- evidence codes and their states (Section 5.4)
print('\nEvidence codes (reported / not reported / not determinable)')
for c, col in CODES:
    k = collections.Counter(s[col] for s in G)
    print('  %s: %d / %d / %d' % (c, k['reported'], k['not reported'], k['not determinable']))
print('  U design:', dict(collections.Counter(s['U_design'] for s in G if has(s, 'U'))))
print('  Reader study and utility experiment both reported:', sum(has(s, 'R') and has(s, 'U') for s in G))
print('  None of the five types:', dict(collections.Counter(s['no_evidence_type'] for s in G if s['no_evidence_type'])))
print('  Code source:', dict(collections.Counter(s['code_source'].split(' (')[0] for s in G)))
print('  Privacy assessment (the studies whose intended use is privacy-preserving sharing):', sum(s['intended_use'] == 'Privacy-preserving data sharing' for s in G))

# ---------------- Section 3.3: text form, auxiliary input and sensitivity subsets
print('\nText form x auxiliary input:', dict(collections.Counter((s['text_form'], s['auxiliary_input']) for s in G)))
free = [s for s in G if s['text_form'] == 'free text']
scratch = [s for s in G if s['edits_existing_image'] == 'no' and s['auxiliary_input'] != 'prior']
both = [s for s in free if s in scratch]
for name, sub in [('All studies', G), ('Free text', free), ('Generation from noise', scratch), ('Free text and generation from noise', both)]:
    print('  %-38s n=%3d  R %s  U %s' % (name, len(sub), pct(sum(has(s, 'R') for s in sub), len(sub)), pct(sum(has(s, 'U') for s in sub), len(sub))))

# ---------------- inter-rater agreement at the eligibility stage (Section 1.3)
try:
    import openpyxl
    ws = openpyxl.load_workbook(os.path.join(ROOT, 'screening', 'screening_log.xlsx'), read_only=True)['S2 Eligibility (276)']
    pairs = [(r[7], r[8]) for r in ws.iter_rows(min_row=2, values_only=True) if r[0] is not None]
    n = len(pairs)
    def kappa(pp):
        po = sum(a == b for a, b in pp) / n
        ca = collections.Counter(a for a, _ in pp); cb = collections.Counter(b for _, b in pp)
        pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
        return sum(a == b for a, b in pp), po, pe, (po - pe) / (1 - pe)
    k10 = kappa(pairs)
    inc = lambda c: 'include' if c in ('G', 'E') else 'exclude'
    k2 = kappa([(inc(a), inc(b)) for a, b in pairs])
    print('\nEligibility, %d reports' % n)
    print('  10 categories: agreement %d (%.1f%%), expected %.1f%%, kappa %.2f' % (k10[0], 100 * k10[1], 100 * k10[2], k10[3]))
    print('  include/exclude: agreement %d (%.1f%%), expected %.1f%%, kappa %.2f' % (k2[0], 100 * k2[1], 100 * k2[2], k2[3]))
    print('  coded eligible: author 1 %d, author 2 %d' % (sum(a in ('G', 'E') for a, _ in pairs), sum(b in ('G', 'E') for _, b in pairs)))
except ImportError:
    print('\nopenpyxl not installed: inter-rater agreement skipped')
