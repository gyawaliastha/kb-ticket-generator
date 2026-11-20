# KB Ticket Generator

Proof-of-concept pipeline that turns resolved IT support tickets into draft knowledge-base (KB) articles using generative AI and Knowledge-Centered Service (KCS) principles. Capstone project, MSIT 5910.

```
tickets (CSV/JSON) -> validate -> anonymize -> extract -> generate draft -> quality checks -> human review -> store/evaluate
```

## Scope
Local Python workflow. Synthetic/anonymized tickets only. No live ticketing integration. Nothing is published without human approval.

## Layout
| Path | Purpose |
|---|---|
| `src/kbgen/` | Pipeline modules |
| `data/sample/` | Synthetic sample tickets |
| `docs/` | Requirements, architecture notes, design diagram |
| `tests/` | Unit tests |
| `outputs/` | Generated drafts and evaluation results |

## Run
```
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m pytest
PYTHONPATH=src python -m kbgen.pipeline data/sample/tickets.csv
```

## Branching
`main` stable milestones, `development` integration, `feature-*` and `docs-*` branches via pull request. Commit style: `feat:`, `fix:`, `docs:`, `test:` with the requirement ID, e.g. `feat: validate required fields (FR2)`.
