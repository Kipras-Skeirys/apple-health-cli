from core.state import get_all_summary_names, add_staged


def add(names: list[str], all_flag: bool) -> None:
    if all_flag:
        add_staged(get_all_summary_names())
    else:
        add_staged(names)
