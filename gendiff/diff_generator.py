import itertools

from gendiff.parser import parse_file


def generate_diff(filepath1, filepath2):
    file1 = parse_file(filepath1)
    file2 = parse_file(filepath2)
    diff = define_diff(file1, file2)
    formated_diff = format_diff(diff, file1, file2)
    return formated_diff


def define_diff(file1, file2):
    keys = file1 | file2
    result = {}
    for key in keys:
        if key not in file2:
            result[key] = "removed"
        elif key not in file1:
            result[key] = "added"
        elif file1[key] == file2[key]:
            result[key] = "unchanged"
        else:
            result[key] = "changed"
    return result


def format_diff(diff, file1, file2):
    lines = []
    for key, status in diff.items():
        match status:
            case "added":
                lines.append(format_line(key, file2[key], "+"))
            case "removed":
                lines.append(format_line(key, file1[key], "-"))
            case "unchanged":
                lines.append(format_line(key, file1[key]))
            case "changed":
                lines.append(format_line(key, file1[key], "-"))
                lines.append(format_line(key, file2[key], "+"))
    lines.sort(key=lambda x: x[4])
    result = itertools.chain("{", lines, "}")
    return "\n".join(result)


def format_line(key, value, symbol=" "):
    if type(value) is bool:
        value = str(value).lower()
    return f"  {symbol} {key}: {value}"
