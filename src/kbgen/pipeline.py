"""Runs ingest -> validate -> anonymize -> prompt. Drafts stay 'draft' until human approval (FR7)."""
import sys
from .ingest import load_tickets, validate_tickets
from .privacy import anonymize_ticket
from .generate import build_prompt


def run(path):
    valid, rejected = validate_tickets(load_tickets(path))
    for r in rejected:
        print(f"REJECTED row {r['row']}: {'; '.join(r['errors'])}")
    results = []
    for i, ticket in enumerate(valid, start=1):
        clean = anonymize_ticket(ticket, i)
        results.append({"reference_id": clean["reference_id"], "status": "draft",
                        "prompt": build_prompt(clean)})
    return results


if __name__ == "__main__":
    for item in run(sys.argv[1]):
        print(item["reference_id"], item["status"])
