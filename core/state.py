import json
from pathlib import Path

from core.errors import AHCliError


STATE_PATH = Path.home() / ".ahcli_state.json"


def _save(state: dict) -> None:
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def _load() -> dict:
    if not STATE_PATH.is_file():
        raise AHCliError("Nothing is mounted. Run 'mount <path>' first")

    try:
        with open(STATE_PATH, "r") as f:
            state = json.load(f)
            _check_state_schema(state)
            return state
    except json.JSONDecodeError:
        raise AHCliError("The state file is damaged. Run 'mount <path>' again")


def _check_state_schema(state: dict) -> None:
    required_keys = {"source", "summary", "staged"}
    if not isinstance(state, dict) or not all(key in state for key in required_keys):
        raise AHCliError("The state file is damaged. Run 'mount <path>' again")


def init_state(source: Path, summary: dict) -> None:
    state = {
        "source": str(source),
        "summary": summary,
        "staged": [],
    }

    _save(state)


def get_state() -> dict:
    return _load()


def get_source() -> Path:
    state = _load()

    return Path(state["source"])


def get_all_summary_names() -> list[str]:
    state = _load()

    return list(state["summary"])


def get_all_staged_names() -> list[str]:
    state = _load()

    return state["staged"]


def add_staged(names: list[str]) -> None:
    state = _load()

    for name in names:
        if name in state["staged"]:
            continue

        if name not in state["summary"]:
            continue

        state["staged"].append(name)

    _save(state)


def remove_staged(names: list[str]) -> None:
    state = _load()
    
    for name in names:
        if name not in state["staged"]:
            continue
        state["staged"].remove(name)

    _save(state)


def remove_all_staged() -> None:
    state = _load()

    state["staged"] = []

    _save(state)
