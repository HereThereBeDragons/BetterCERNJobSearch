# BetterCERNJobSearch

Because Drupal is sooo good...

Better search for keywords and filtering for contract type and grade (for Staff) for: https://careers.cern/alljobs 

## How to use

1) Edit in `better_search_cern_careers.py` lines 19 - 25 to fit your needs
```
contract = "-LD" #-LD, -GRAP, ....
grade = "6-7"
partial_matches = [ #all in caps
  "SOFTWARE",
  "DEVELOPER",
  "ENGINEER",
]
```
(`grade` is only for `LD`)

2) Run `python3 better_search_cern_careers.py`

3) Output is something like:
```
Looking for fitting jobs
Contract -LD
Grade 6-7
Partial matches in job description ['SOFTWARE', 'DEVELOPER', 'ENGINEER']

Matches found:
ENGINEER / APPLIED PHYSICIST IN THERMODYNAMICS (TE-CRG-CL-2024-56-LD)	 https://www.smartrecruiters.com/CERN/743999981275765-engineer-applied-physicist-in-thermodynamics-te-crg-cl-2024-56-ld-
SCIENTIFIC SOFTWARE ENGINEER - DATA ANALYSIS (EP-SFT-2024-55-LD)	 https://www.smartrecruiters.com/CERN/743999980742256-scientific-software-engineer-data-analysis-ep-sft-2024-55-ld-
QUANTUM COMPUTING ENGINEER (IT-GOV-INN-2024-38-LD)	 https://www.smartrecruiters.com/CERN/743999980711255-quantum-computing-engineer-it-gov-inn-2024-38-ld-
```
