import xml.etree.ElementTree as ET

from core.errors import AHCliError


PREFIXES = [
    "HKQuantityTypeIdentifier",
    "HKCategoryTypeIdentifier",
    "HKCharacteristicTypeIdentifier",
    "HKWorkoutActivityType",
    "HKDataType",
]


def validate_file(path):
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


def build_summary(path) -> dict:
    summary = {}

    context = ET.iterparse(path, events=("start", "end"))

    try:
        depth = 0
        root = None

        for event, elem in context:
            if event == "end":
                depth -= 1
                if depth == 1:
                    root.clear()
                else:
                    elem.clear()
                continue

            if root is None:
                root = elem
            depth += 1

            if elem.tag == "Record" and depth == 2:
                data_type_name = short_name(elem.get("type"))
                if data_type_name not in summary:
                    summary[data_type_name] = {"count": 0}
                summary[data_type_name]["count"] += 1
    except ET.ParseError:
        raise AHCliError(f"'{path}' appears to be damaged or incomplete")

    return summary


def short_name(identifier) -> str:
    for prefix in PREFIXES:
        if identifier.startswith(prefix):
            return identifier.removeprefix(prefix)

    return identifier


def mount(path):
    validate_file(path)
    summary = build_summary(path)
