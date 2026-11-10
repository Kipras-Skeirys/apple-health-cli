from core.state import get_state, add_staged


def add(names: list[str], all_flag: bool) -> None:
    state = get_state()

    if all_flag:
        add_staged(list(state["summary"]))
    else:
        add_staged(names)
