from pathlib import Path
import xml.etree.ElementTree as ET

from core.errors import AHCliError
from core.state import get_source, get_all_staged_names
from core.names import short_name


def export(path: Path) -> None:
    mount_source = get_source()
    staged = get_all_staged_names()

    if path.is_dir():
        path = path / "export.xml"

    if path.suffix != ".xml":
        raise AHCliError(f"'{path.name}': is not a supported file format. Exports only as XML files.")

    if not path.parent.is_dir():
        raise AHCliError(f"'{path.parent}': directory does not exist")

    if path == mount_source:
        raise AHCliError("You cannot overwrite the same file that you mounted. Choose a different export path or choose a custom file name")

    try:
        with open(path, "w", encoding="utf-8") as out:
            with open(mount_source, "r", encoding="utf-8") as source:
                for line in source:
                    out.write(line)
                    if line.startswith("<HealthData"):
                        break

            context = ET.iterparse(mount_source, events=("end", "start"))

            depth = 0
            root = None

            for event, elem in context:
                if root is None:
                    root = elem

                if event == "start":
                    if depth == 1:
                        root.clear()
                    depth += 1
                    continue

                # "end" event
                if depth == 2:
                    if elem.tag != "Record" or short_name(elem.get("type")) in staged:
                        out.write(ET.tostring(elem, encoding="unicode"))
                    elem.clear()
                depth -= 1

            out.write("</HealthData>\n")
    except ET.ParseError:
        path.unlink(missing_ok=True)
        raise AHCliError(f"Export failed. '{mount_source}' appears to be damaged or incomplete")
    except FileNotFoundError:
        path.unlink(missing_ok=True)
        raise AHCliError(f"Export failed. '{mount_source}' appears to be missing")
    except BaseException:
        path.unlink(missing_ok=True)
        raise

