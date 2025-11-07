import pytest
from script_bugs import compute_focus_level, select_tasks, estimate_durations

def test_compute_focus_level_high(capfd):
    compute_focus_level(8)
    out, _ = capfd.readouterr()
    assert "High" in out

def test_compute_focus_level_medium(capfd):
    compute_focus_level(6)
    out, _ = capfd.readouterr()
    assert "Medium" in out

def test_select_tasks_low():
    tasks = select_tasks("Low")
    assert "Break" in tasks
    assert "Meditation" in tasks

def test_estimate_durations_returns_correct_values():
    durations = estimate_durations(["Deep Work", "Team Sync"])
    assert durations["Deep Work"] == 180
    assert durations["Team Sync"] == 30
