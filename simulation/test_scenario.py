import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("generate_scenario.py")
SPEC = importlib.util.spec_from_file_location("scenario_generator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_dataset_is_deterministic_and_synthetic():
    first = MODULE.build_scenario()
    second = MODULE.build_scenario()
    assert first == second
    assert len(first) == 49
    assert all(row["simulation"] is True for row in first)
    assert all(row["source"] == "synthetic-training-data" for row in first)


def test_attack_story_has_expected_stages():
    rows = MODULE.build_scenario()
    phases = {row.get("phase") for row in rows}
    assert {"reconnaissance", "credential-access", "initial-access", "execution", "persistence"} <= phases
    failures = [r for r in rows if r.get("event_type") == "ssh_auth" and r.get("auth_result") == "failure" and r.get("scenario_id") == "SOC-CASE-001"]
    successes = [r for r in rows if r.get("event_type") == "ssh_auth" and r.get("auth_result") == "success" and r.get("scenario_id") == "SOC-CASE-001"]
    assert len(failures) == 12
    assert len(successes) == 1


def test_benign_activity_is_separate():
    rows = MODULE.build_scenario()
    benign = [r for r in rows if r.get("scenario_id") == "BENIGN-OPS-001"]
    assert len(benign) == 4
    assert all(r["src_ip"] == "192.168.100.5" for r in benign)
