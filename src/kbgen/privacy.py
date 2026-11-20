"""Module 2: preprocessing and privacy filtering (FR3)."""
import re
import hashlib

PATTERNS = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[EMAIL]"),
    (re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), "[IP_ADDRESS]"),
    (re.compile(r"\+?\d[\d\s().-]{8,}\d"), "[PHONE]"),
    (re.compile(r"(?i)\b(?:password|passwd|pwd|token|api[_-]?key|secret)\s*[:=]\s*\S+"), "[SECRET]"),
]


def mask_text(text):
    """Mask emails, IP addresses, phone numbers, and credential-like strings."""
    text = " ".join(str(text).split())
    for pattern, label in PATTERNS:
        text = pattern.sub(label, text)
    return text


def reference_id(ticket, index):
    """Stable reference ID so articles trace to a source without exposing identifiers."""
    raw = f"{index}:{ticket.get('title', '')}:{ticket.get('description', '')}"
    return "TKT-" + hashlib.sha256(raw.encode()).hexdigest()[:8].upper()


def anonymize_ticket(ticket, index=0):
    out = {k: mask_text(v) for k, v in ticket.items()}
    out["reference_id"] = reference_id(ticket, index)
    return out
