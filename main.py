from pathlib import Path
import sys
import argparse

from commands.mount import mount
from commands.status import status
from core.errors import AHCliError


def main() -> None:
    parser = argparse.ArgumentParser(description="Edit Apple Health export data")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_mount = subparsers.add_parser("mount")
    parser_mount.add_argument("path", type=Path)

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("data_types")

    subparsers.add_parser("status")

    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("data_types")

    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("data_types")

    subparsers.add_parser("export")

    args = parser.parse_args() 
    try:
        match args.command:
            case "mount":
                mount(args.path)
            case "add":
                raise AHCliError(f"'{args.command}': command isn't implemented yet")
            case "status":
                status()
            case "edit":
                raise AHCliError(f"'{args.command}': command isn't implemented yet")
            case "remove":
                raise AHCliError(f"'{args.command}': command isn't implemented yet")
            case "export":
                raise AHCliError(f"'{args.command}': command isn't implemented yet")
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
