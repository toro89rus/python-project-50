from gendiff.parser import parse_file
from gendiff.formatters import stylish, plain, json


def generate_diff(filepath1, filepath2, format="stylish"):
    file1 = parse_file(filepath1)
    file2 = parse_file(filepath2)
    diff = define_diff(file1, file2)
    match format:
        case "stylish":
            formated_diff = stylish.format_diff(diff)
        case "plain":
            formated_diff = plain.format_diff(diff)
        case "json":
            formated_diff = json.format_diff(diff)
    return formated_diff


def define_diff(tree1, tree2):
    result = {}
    keys = sorted(tree1 | tree2)
    for key in keys:
        if key not in tree2:
            result[key] = {"status": "removed", "value": tree1[key]}
        elif key not in tree1:
            result[key] = {"status": "added", "value": tree2[key]}
        elif tree1[key] == tree2[key]:
            result[key] = {"status": "unchanged", "value": tree1[key]}
        elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):
            result[key] = {
                "status": "nested",
                "value": define_diff(tree1[key], tree2[key]),
            }
        else:
            result[key] = {
                "status": "changed",
                "value": (tree1[key], tree2[key]),
            }
    return result
