import argparse


def main():
    parser = argparse.ArgumentParser(description="Edit Apple Health export data")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_mount = subparsers.add_parser("mount")
    parser_mount.add_argument("path")

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("data_types")

    subparsers.add_parser("status")

    parser_edit = subparsers.add_parser("edit")
    parser_edit.add_argument("data_types")

    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument("data_types")

    subparsers.add_parser("export")

    args = parser.parse_args()

    match args.command:
        case "mount":
            pass
        case "add":
            pass
        case "status":
            pass
        case "edit":
            pass
        case "remove":
            pass
        case "export":
            pass
        case _:
            pass
        
if __name__ == "__main__":
    main()