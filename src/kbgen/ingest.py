"""Module 1: ticket ingestion and validation (FR1, FR2)."""
import csv
import json
from pathlib import Path

REQUIRED_FIELDS = ["title", "description", "category", "resolution"]
OPTIONAL_FIELDS = ["troubleshooting_notes"]


def load_tickets(path):
    """Load tickets from a CSV or JSON file and return a list of dicts."""
    path = Path(path)
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    if path.suffix.lower() == ".json":
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data]
    raise ValueError(f"Unsupported file type: {path.suffix}")


def validate_tickets(tickets):
    """Split tickets into (valid, rejected). Rejected items carry error messages.

    Invalid records are flagged, never silently processed.
    """
    valid, rejected, seen = [], [], set()
    for i, t in enumerate(tickets, start=1):
        errors = [f"missing or empty field: {k}" for k in REQUIRED_FIELDS
                  if not str(t.get(k, "") or "").strip()]
        key = (str(t.get("title", "")).strip().lower(), str(t.get("description", "")).strip().lower())
        if not errors and key in seen:
            errors.append("duplicate ticket")
        seen.add(key)
        if errors:
            rejected.append({"row": i, "ticket": t, "errors": errors})
        else:
            valid.append(t)
    return valid, rejected
