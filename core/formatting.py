def format_size(size: int) -> str:
    unit_list = ["B", "KB", "MB", "GB", "TB"]
    unit = 0

    while size >= 1024 and unit < len(unit_list) - 1:
        size = size / 1024
        unit += 1

    return f"{size:.1f} {unit_list[unit]}"
