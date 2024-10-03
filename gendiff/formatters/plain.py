from gendiff.parser import parse_file

file1 = parse_file("tests/fixtures/flat1.json")
file2 = parse_file("tests/fixtures/flat2.json")


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if type(value) is bool:
        return str(value).lower()
    if value is None:
        return "null"
    return f"'{value}'"


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
