from core.errors import AHCliError
import xml.etree.ElementTree as ET


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

def mount(path):
    validate_file(path)
    pass