import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("generate_scenario.py")
SPEC = importlib.util.spec_from_file_location("scenario_generator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SPL = SCRIPT.parents[1] / "splunk" / "simulation_detections.spl"


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
    assert max(r["_time"] for r in failures) < successes[0]["_time"]


def test_benign_activity_is_separate():
    rows = MODULE.build_scenario()
    benign = [r for r in rows if r.get("scenario_id") == "BENIGN-OPS-001"]
    assert len(benign) == 4
    assert all(r["src_ip"] == "192.168.100.5" for r in benign)


def test_fixture_has_all_four_detection_prerequisites():
    rows = MODULE.build_scenario()
    assert len({r["dest_port"] for r in rows if r.get("event_type") == "connection_attempt"}) == 30
    assert any(r.get("event_type") == "process_exec" and r.get("user") == "www-data" and r.get("exe") == "/bin/bash" for r in rows)
    assert any(r.get("event_type") == "file_change" and "/crontabs/" in r.get("path", "") and r.get("operation") == "modified" for r in rows)


def test_spl_uses_event_fields_and_time_window_correlation():
    query = SPL.read_text(encoding="utf-8")
    assert "streamstats time_window=120s" in query
    assert "streamstats time_window=300s current=f" in query
    assert query.count('event_type=process_exec') == 1
    assert query.count('event_type=file_change') == 1
    assert "index=soc_simulation simulation=true sourcetype=linux_audit" not in query
    assert 'index=soc_simulation simulation=true' in query
