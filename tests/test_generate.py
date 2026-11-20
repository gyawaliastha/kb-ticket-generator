from kbgen.generate import build_prompt, check_draft, SECTIONS


def test_prompt_marks_missing_fields_and_includes_reference():
    p = build_prompt({"title": "VPN", "resolution": "Reset", "reference_id": "TKT-1"})
    assert "not documented" in p and "TKT-1" in p


def test_check_draft_detects_missing_sections():
    assert any("Resolution" in x for x in check_draft("Title\nIssue Summary"))


def test_complete_draft_has_no_missing_sections():
    assert not [p for p in check_draft("\n".join(SECTIONS)) if p.startswith("missing")]
