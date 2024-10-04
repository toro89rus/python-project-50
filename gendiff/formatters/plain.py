def format_value(value):
    if isinstance(value, dict):
        result = "[complex value]"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, int):
        result = value
    elif value is None:
        result = "null"
    else:
        result = f"'{value}'"
    return result


def format_line(path, value, status):
    if len(path) > 1:
        str_path = ".".join(path)
    else:
        [str_path] = path
    match status:
        case "removed":
            return f"Property '{str_path}' was removed"
        case "added":
            return (
                f"Property '{str_path}' was added"
                f" with value: {format_value(value)}"
            )
        case "changed":
            old, new = value
            return (
                f"Property '{str_path}' was updated."
                f" From {format_value(old)} to {format_value(new)}"
            )


def format_diff(diff):
    lines = []

    def walk(node, path):
        for key, child in node.items():
            status = child["status"]
            value = child["value"]
            match status:
                case "unchanged":
                    continue
                case "nested":
                    walk(value, path + [key])
                case _:
                    lines.append(format_line(path + [key], value, status))
    walk(diff, [])
    return "\n".join(lines)
