# Text-Conditioned Medical Image Synthesis: A Systematic Review of Evaluation Practices

This repository holds the search strings, screening records, study-level data and code behind the systematic review *Text-Conditioned Medical Image Synthesis: A Systematic Review of Evaluation Practices*. With these files every count in the PRISMA flow diagram (Figure 1), in Tables 3 and 4 and in Sections 1.3, 3.3 and 5.4 of the article can be traced to individual records and recomputed.

## Contents

| Path | Content | Article |
|---|---|---|
| `search/search_strings.md` | Full search strings for Scopus, Web of Science Core Collection and PubMed, with the number of records each returned (searched 18 November 2026) | Section 1.3; PRISMA 2020 item 7 |
| `code/deduplicate.py` | Deduplication rule: DOI, normalized title and approximate title matching | Section 1.3 |
| `code/keyword_filter.py` | Documented keyword filter applied before screening | Section 1.3 |
| `screening/screening_log.xlsx` | Every record with its decision: S0, the 1,772 records removed by the original keyword filter; S1, title and abstract screening of 733 records (model suggestion and final decision of the two authors); S2, eligibility assessment of 276 reports with the independent code of each author and the final decision | Figure 1; Section 1.3 |
| `screening/prisma_flow_diagram.png` | PRISMA 2020 flow diagram | Figure 1 |
| `screening/keyword_filter_audit.xlsx` | Audit of the keyword filter: the 58 records retained only by the documented rule and a random sample of 150 of the 1,714 records removed by both filters | Section 1.3 |
| `data/included_studies_generative.csv` | Study-level matrix of the 131 generative studies: DOI, inclusion category, modality, dimensionality, conditioning axis, form of the text, auxiliary input, editing, approach, adaptation, intended use, the five evidence codes with their state (reported, not reported, not determinable), the design of the utility experiment and the source of the codes (abstract or full text) | Tables 3 and 4; Sections 3.3 and 5.4 |
| `data/included_studies_general_purpose.csv` | The 33 evaluations of general-purpose generators: tools, task and main finding | Table 5 |
| `data/excluded_reports.csv` | The 110 reports excluded at the eligibility stage, with their exclusion code | Figure 1 |
| `data/report_study_map.csv` | Links the 166 included reports to the 164 studies | Section 1.3 |
| `code/reproduce_counts.py` | Recomputes the counts reported in the article, including Cohen's κ at the eligibility stage | Tables 3 and 4; Sections 1.3, 3.3 and 5.4 |

## Reproducing the counts

```
pip install openpyxl
python code/reproduce_counts.py
```

The script prints the counts by year, the rows of Table 3, the category counts of Table 4, the state of each evidence code, the design of the utility experiments, the sensitivity subsets of Section 3.3 and the inter-rater agreement at the eligibility stage.

## Evidence codes

| Code | Meaning |
|---|---|
| F | Image fidelity or distribution metric (for example FID, KID, SSIM) |
| A | Text–image alignment metric, including a classifier or vision–language model applied to generated images to check that the requested finding is present |
| R | Assessment of generated images by clinicians or other domain experts |
| U | Generated images added to the training data of another model that was then tested on real images, or used as test data for an existing model |
| S | Results reported by patient subgroup |

Each code has one of three states: *reported*, *not reported* in the sources we read, or *not determinable* when neither the abstract nor an accessible full text allowed classification. The codes record which types of evaluation a study reports, not how well the evaluation was designed.

## Eligibility decision codes

| Code | Meaning |
|---|---|
| G | Included: generative text-to-medical image study |
| E | Included: evaluation of a general-purpose generator on medical content |
| X1 | Images are not medical images |
| X3 | Depiction of clinicians or patients by general-purpose tools (representation, not medical images) |
| X4 | Text only selects the target domain of an image-to-image, restoration or reconstruction task |
| X5 | Conditioning on images, masks, labels or metadata without text |
| X6 | Review, commentary, editorial, news item, meeting abstract or front matter without an original experiment |
| X7 | Benchmark or analysis without a new generator |
| X8 | No image output (report generation, retrieval, segmentation, registration) |
| X9 | Preprint or other work not peer reviewed |

## Notes

- Abstracts are not reproduced because the terms of the bibliographic databases restrict their redistribution; each record can be retrieved through its DOI or title.
- Years in the study-level matrix are those of the reference-list entry, that is, of the journal issue or proceedings volume; years in the screening log are those of the database record.
- A large language model suggested the decisions at the title and abstract stage and the eligibility codes; the model's suggestions, the authors' codes and the final decisions are kept in separate columns (Section 1.3 of the article).

## Citation

If you use these files, please cite the article. [Authors: add the full reference and DOI after publication.]

## License

[Authors: choose a license, for example CC BY 4.0 for the data and MIT for the code.]
