from gendiff.formatters.format_selector import format_diff
from gendiff.parser import parse_content


def generate_diff(filepath1, filepath2, format="stylish"):
    dict1 = parse_content(filepath1)
    dict2 = parse_content(filepath2)
    diff = build_diff_tree(dict1, dict2)
    formated_diff = format_diff(diff, format)
    return formated_diff


def build_diff_tree(tree1, tree2):
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
                "value": build_diff_tree(tree1[key], tree2[key]),
            }
        else:
            result[key] = {
                "status": "changed",
                "value": (tree1[key], tree2[key]),
            }
    return result
