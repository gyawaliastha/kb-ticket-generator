from kbgen.privacy import mask_text, anonymize_ticket


def test_email_and_ip_masked():
    out = mask_text("User jane.doe@corp.com on 10.1.2.3 failed")
    assert "jane.doe@corp.com" not in out and "10.1.2.3" not in out
    assert "[EMAIL]" in out and "[IP_ADDRESS]" in out


def test_secret_masked():
    assert "hunter2" not in mask_text("password: hunter2")


def test_reference_id_added_and_stable():
    t = {"title": "a", "description": "b"}
    assert anonymize_ticket(t, 1)["reference_id"] == anonymize_ticket(t, 1)["reference_id"]
