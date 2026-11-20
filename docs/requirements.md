# Requirements

## Functional
| ID | Requirement | Module |
|---|---|---|
| FR1 | Import CSV/JSON tickets | ingest |
| FR2 | Validate required fields, report invalid records | ingest |
| FR3 | Mask sensitive strings before AI processing | privacy |
| FR4 | Extract issue context from ticket fields | generate |
| FR5 | Generate structured KB draft from approved template | generate |
| FR6 | Flag missing information and unsupported claims | generate |
| FR7 | Reviewer can edit, reject, or approve drafts | review (planned) |
| FR8 | Save drafts/approved articles with source reference and status | storage (planned) |
| FR9 | Evaluate accuracy, completeness, readability, usefulness | evaluation (planned) |
| FR10 | Export articles and evaluation results | storage (planned) |

## Non-functional
Performance (small dataset), usability (clear errors/headings), reliability (no falsely approved articles), scalability (modular), security/privacy (synthetic data, masking, no secrets in code), maintainability (tests, versioned prompts), fairness (one rubric), human oversight (approval gate).
