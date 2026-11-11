from pathlib import Path
import sys
import argparse

from commands.mount import mount
from commands.status import status
from commands.add import add
from commands.remove import remove
from commands.export import export
from core.errors import AHCliError


def absolute_path(path: str) -> Path:
    return Path(path).expanduser().resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description="Edit Apple Health export data")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_mount = subparsers.add_parser("mount")
    parser_mount.add_argument("path", type=absolute_path)

    parser_add = subparsers.add_parser("add")
    group_add = parser_add.add_mutually_exclusive_group(required=True)
    group_add.add_argument("data_names", type=str, nargs="*")
    group_add.add_argument("-a", "--all", action="store_true")

    subparsers.add_parser("status")

    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("data_names")

    parser_remove = subparsers.add_parser("remove")
    group_remove = parser_remove.add_mutually_exclusive_group(required=True)
    group_remove.add_argument("data_names", type=str, nargs="*")
    group_remove.add_argument("-a", "--all", action="store_true")

    parser_export = subparsers.add_parser("export")
    parser_export.add_argument("export_path", type=absolute_path, nargs="?", default=".")

    args = parser.parse_args()

    try:
        match args.command:
            case "mount":
                mount(args.path)
            case "add":
                add(args.data_names, args.all)
            case "status":
                status()
            case "edit":
                raise AHCliError(f"'{args.command}': command isn't implemented yet")
            case "remove":
                remove(args.data_names, args.all)
            case "export":
                export(args.export_path)
            case _:
                raise AHCliError(f"'{args.command}': command does not exist")
    except AHCliError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Permission denied: '{e.filename}'. Check the file's permissions.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
