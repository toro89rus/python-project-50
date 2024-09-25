import itertools
import json


def parse_json(filename):
    data = json.load(open(filename))
    return data


def generate_diff(filepath1, filepath2):
    file1 = parse_json(filepath1)
    file2 = parse_json(filepath2)
    diff = define_diff(file1, file2)
    formated_diff = format_diff(diff, file1, file2)
    return formated_diff


def define_diff(file1, file2):
    set_1 = set(file1)
    set_2 = set(file2)

    result = {
        "kept": set_1 & set_2,
        "added": set_2 - set_1,
        "removed": set_1 - set_2,
    }
    result["changed"] = set()
    result["unchanged"] = set()
    for kept_string in result["kept"]:
        if file1[kept_string] == file2[kept_string]:
            result["unchanged"].add(kept_string)
        else:
            result["changed"].add(kept_string)
    result.pop("kept")
    return result


def format_diff(diff, file1, file2):
    lines = []
    for key, values in diff.items():
        for value in values:
            match key:
                case "added":
                    lines.append(format_line(value, file2[value], "+"))
                case "removed":
                    lines.append(format_line(value, file1[value], "-"))
                case "unchanged":
                    lines.append(format_line(value, file1[value]))
                case "changed":
                    lines.append(format_line(value, file1[value], "-"))
                    lines.append(format_line(value, file2[value], "+"))
    lines.sort(key=lambda x: x[4])
    result = itertools.chain("{", lines, "}")
    return "\n".join(result)


def format_line(key, value, symbol=" "):
    if type(value) is bool:
        value = str(value).lower()
    return f"  {symbol} {key}: {value}"
