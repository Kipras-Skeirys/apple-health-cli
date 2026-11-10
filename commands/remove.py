from core.state import remove_staged, remove_all_staged


def remove(names: list[str], all_flag: bool) -> None:
    if all_flag:
        remove_all_staged()
    else:
        remove_staged(names)
