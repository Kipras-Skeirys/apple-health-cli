from core.state import get_state


def status():
    state = get_state()
    available = {}
    staged = {}

    for name, value in state["summary"].items():
        if name in state["staged"]:
            staged[name] = value
        else:
            available[name] = value

    width = len(max(state["summary"], key=len, default="")) + 2

    print("\n")
    print(f"\tAvailable ({len(available)})")

    for name, value in available.items():
        print(f"\t\t{name:<{width}} | {value['count']}")

    print(f"\n\tStaged ({len(staged)})")

    if not staged:
        print("\t\tNothing staged. Use 'add <data types>'")
    else:
        for name, value in staged.items():
            print(f"\t\t{name:<{width}} | {value['count']}")

    print("\n")
