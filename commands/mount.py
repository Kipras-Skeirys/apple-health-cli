import xml.etree.ElementTree as ET
from pathlib import Path

from core.errors import AHCliError
from core.state import init_state
from core.names import short_name


def validate_file(path: Path) -> None:
    if not path.exists():
        raise AHCliError(f"'{path}' does not exist")
    if not path.is_file():
        raise AHCliError("You selected a directory, please select a valid Apple Health export XML file")

    context = ET.iterparse(path, events=("start",))
    try:
        event, first_elem = next(context)
    except ET.ParseError:
        raise AHCliError(f"'{path}' is not a valid XML file")
    if first_elem.tag != "HealthData":
        raise AHCliError(f"'{path}' does not contain valid Apple Health data")


def get_size(elem: ET.Element) -> int:
    return len(ET.tostring(elem, encoding="utf-8"))


def build_summary(path: Path) -> dict:
    summary = {}

    context = ET.iterparse(path, events=("start", "end"))

    try:
        depth = 0
        root = None

        for event, elem in context:
            if event == "start":
                if root is None:
                    root = elem
                depth += 1
                continue

            if elem.tag == "Record" and depth == 2:
                data_type_name = short_name(elem.get("type"))
                if data_type_name not in summary:
                    summary[data_type_name] = {
                        "count": 0,
                        "size": 0,
                    }
                summary[data_type_name]["size"] += get_size(elem)
                summary[data_type_name]["count"] += 1

            depth -= 1
            if depth == 1:
                root.clear()
    except ET.ParseError:
        raise AHCliError(f"'{path}' appears to be damaged or incomplete")

    return summary


def mount(path: Path) -> None:
    validate_file(path)
    summary = build_summary(path)
    init_state(path, summary)
