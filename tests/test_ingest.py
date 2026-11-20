from kbgen.ingest import validate_tickets


def ticket(**kw):
    base = {"title": "VPN fails", "description": "Cannot connect", "category": "network", "resolution": "Reset profile"}
    base.update(kw)
    return base


def test_valid_ticket_passes():
    valid, rejected = validate_tickets([ticket()])
    assert len(valid) == 1 and not rejected


def test_missing_resolution_is_rejected():
    valid, rejected = validate_tickets([ticket(resolution="  ")])
    assert not valid and "resolution" in rejected[0]["errors"][0]


def test_duplicates_are_flagged():
    valid, rejected = validate_tickets([ticket(), ticket()])
    assert len(valid) == 1 and rejected[0]["errors"] == ["duplicate ticket"]
