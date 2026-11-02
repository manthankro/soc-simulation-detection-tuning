import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "attack-scripts" / "generate_sample_events.py"
SPEC = importlib.util.spec_from_file_location("event_generator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_build_events_are_synthetic_and_structured():
    events = list(MODULE.build_events())
    assert len(events) == 5
    assert all(event["simulation"] is True for event in events)
    assert all("timestamp" in event for event in events)
    assert all("event_type" in event for event in events)
