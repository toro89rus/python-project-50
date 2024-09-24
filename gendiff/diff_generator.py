import json
import itertools


def parse_json(filename):
    data = json.load(open(filename))
    return data


def generate_diff(filepath1, filepath2):
    file1 = parse_json(filepath1)
    file2 = parse_json(filepath2)
    lines = []
    keys_diff = define_keys_diff(file1, file2)

    for key in keys_diff["kept"]:
        if file1[key] == file2[key]:
            lines.append(format_line(key, file1[key]))
        else:
            lines.append(format_line(key, file1[key], "-"))
            lines.append(format_line(key, file2[key], "+"))

    for key in keys_diff["added"]:
        lines.append(format_line(key, file2[key], "+"))

    for key in keys_diff["removed"]:
        lines.append(format_line(key, file1[key], "-"))

    lines.sort(key=lambda x: x[2])
    result = itertools.chain('{', lines, '}')
    return '\n'.join(result)


def define_keys_diff(file1, file2):
    set_1 = set(file1)
    set_2 = set(file2)

    return {
        "kept": set_1 & set_2,
        "added": set_2 - set_1,
        "removed": set_1 - set_2
        }


def format_line(key, value, symbol=" "):
    if type(value) is bool:
        value = str(value).lower()
    return f"{symbol} {key}: {value}"
