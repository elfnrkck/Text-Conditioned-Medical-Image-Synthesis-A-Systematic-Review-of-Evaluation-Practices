# Search strings

All three databases were searched on 18 November 2026. Records were limited to English and to publication from 2016 onwards.

| Database | Fields | Records |
|---|---|---|
| Scopus | Title, abstract and keywords | 2,129 |
| Web of Science Core Collection | Topic | 1,526 |
| PubMed | Title and abstract, with one MeSH term | 310 |
| Total | | 3,965 |

## Scopus

```
TITLE-ABS-KEY ( ( "text-to-image" OR "text to image" OR "text-to-medical" OR "text conditioned" OR "text-conditioned" OR "text conditional" OR "text guided" OR "text-guided" OR "text driven" OR "text-driven" OR "text prompt*" OR "report conditioned" OR "report-conditioned" OR "report guided" OR "report-to-image" OR "language-guided" OR "prompt-guided" ) AND ( generat* OR synthes* OR diffusion OR "generative adversarial" OR gan OR gans ) AND ( medical OR clinical OR biomedical OR radiolog* OR radiograph* OR "x-ray*" OR "computed tomography" OR ct OR mri OR "magnetic resonance" OR patholog* OR histopatholog* OR endoscop* OR colonoscop* OR dermatolog* OR dermoscop* OR fundus OR ophthalm* OR ultrasound OR ultrason* OR mammogra* ) ) AND PUBYEAR > 2015 AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```

## Web of Science Core Collection

```
TS=( ("text-to-image" OR "text to image" OR "text-to-medical" OR "text conditioned" OR "text conditional" OR "text guided" OR "text driven" OR "text prompt*" OR "report conditioned" OR "report guided" OR "report-to-image" OR "language-guided" OR "prompt-guided") AND (generat* OR synthes* OR diffusion OR "generative adversarial" OR GAN OR GANs) AND (medical OR clinical OR biomedical OR radiolog* OR radiograph* OR "x-ray*" OR "computed tomography" OR CT OR MRI OR "magnetic resonance" OR patholog* OR histopatholog* OR endoscop* OR colonoscop* OR dermatolog* OR dermoscop* OR fundus OR ophthalm* OR ultrasound OR ultrason* OR mammogra*) ); publication years 2016–2026; language English
```

## PubMed

```
("text-to-image"[tiab] OR "text to image"[tiab] OR "text-to-medical"[tiab] OR "text conditioned"[tiab:~3] OR "text conditional"[tiab:~3] OR "text guided"[tiab:~3] OR "text driven"[tiab:~3] OR "text prompt*"[tiab] OR "report conditioned"[tiab:~3] OR "report guided"[tiab:~3] OR "report-to-image"[tiab] OR "language-guided"[tiab] OR "prompt-guided"[tiab]) AND (generat*[tiab] OR synthes*[tiab] OR diffusion[tiab] OR "generative adversarial"[tiab] OR GAN[tiab] OR GANs[tiab]) AND (medical[tiab] OR clinical[tiab] OR biomedical[tiab] OR radiolog*[tiab] OR radiograph*[tiab] OR "x-ray*"[tiab] OR "computed tomography"[tiab] OR CT[tiab] OR MRI[tiab] OR "magnetic resonance"[tiab] OR patholog*[tiab] OR histopatholog*[tiab] OR endoscop*[tiab] OR colonoscop*[tiab] OR dermatolog*[tiab] OR dermoscop*[tiab] OR fundus[tiab] OR ophthalm*[tiab] OR ultrasound[tiab] OR ultrason*[tiab] OR mammogra*[tiab] OR "Diagnostic Imaging"[Mesh]) AND ("2016/01/01"[dp] : "2026/12/31"[dp]) AND English[la]
```

Citation searching: backward and forward citation searching of the included studies and of the related reviews in Table 1 of the article added four peer-reviewed reports (sheet S2 of the screening log, IDs C1 to C4). Preprint servers were not searched.
