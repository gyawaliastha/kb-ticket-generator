from kbgen.pipeline import run


def test_pipeline_rejects_incomplete_and_masks_pii():
    results = run("data/sample/tickets.csv")
    assert len(results) == 2                      # third ticket has no resolution
    assert all(r["status"] == "draft" for r in results)
    assert not any("jane.doe@example.com" in r["prompt"] for r in results)
