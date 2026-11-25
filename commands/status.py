from core.state import get_state
from core.formatting import format_size


def _format_row(name: str, value: dict, width: int) -> str:
    name_string = f"{name} ({value['count']})"
    return f"\t\t{name_string:<{width}} | {format_size(value['size'])}"


def status() -> None:
    state = get_state()
    available = {}
    staged = {}

    for name, value in state["summary"].items():
        if name in state["staged"]:
            staged[name] = value
        else:
            available[name] = value

    name_width = len(max(state["summary"], key=len, default=""))
    count_width = len(max((str(value["count"]) for value in state["summary"].values()), key=len, default=""))
    width = name_width + count_width + 5

    print("\n")
    print(f"\tAvailable ({len(available)})")

    for name, value in available.items():
        print(_format_row(name, value, width))

    print(f"\n\tStaged ({len(staged)})")

    if not staged:
        print("\t\tNothing staged. Use 'add <data types>'")
    else:
        for name, value in staged.items():
            print(_format_row(name, value, width))

    print("\n")
