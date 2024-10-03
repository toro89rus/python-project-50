import itertools

from gendiff.parser import parse_file

NEW = "+ "
OLD = "- "
STATIC = "  "
INDENT_SIZE = 4
INDENT_SYMBOL = " "


def generate_diff(filepath1, filepath2):
    file1 = parse_file(filepath1)
    file2 = parse_file(filepath2)
    diff = define_diff(file1, file2)
    formated_diff = format_diff(diff)
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


def get_indents(depth, separator=INDENT_SYMBOL):
    opening_indent_size = depth * INDENT_SIZE + 2
    opening_indent = separator * opening_indent_size
    closing_indent_size = depth * 4
    closing_indent = separator * closing_indent_size
    return (opening_indent, closing_indent)


def format_value(value, depth):
    if type(value) is bool:
        return str(value).lower()
    if value is None:
        return "null"
    if type(value) is dict:
        lines = []
        depth += 1
        for key, nested_value in value.items():
            # if space for  non-existing values is not needed ->
            # add check if format_value(nested_value, depth) is None ->
            # lines.append( ->
            # f"{indent}{STATIC}{key}:}" ->
            # ) ->
            # continue
            indent, closing_indent = get_indents(depth)
            lines.append(
                f"{indent}{STATIC}{key}: {format_value(nested_value, depth)}"
            )
        result = itertools.chain("{", lines, [closing_indent + "}"])
        return "\n".join(result)
    return value


def format_diff(diff):

    def walk(node, depth):
        lines = []
        indent, closing_indent = get_indents(depth)
        for key, child in node.items():
            status = child["status"]
            value = child["value"]
            match status:
                case "nested":
                    lines.append(
                        f"{indent}{STATIC}{key}: {walk(value, depth + 1)}"
                    )
                case "removed":
                    lines.append(
                        f"{indent}{OLD}{key}: {format_value(value, depth)}"
                    )
                case "added":
                    lines.append(
                        f"{indent}{NEW}{key}: {format_value(value, depth)}"
                    )
                case "changed":
                    old, new = value
                    lines.append(
                        f"{indent}{OLD}{key}: {format_value(old, depth)}"
                    )
                    lines.append(
                        f"{indent}{NEW}{key}: {format_value(new, depth)}"
                    )
                case "unchanged":
                    lines.append(
                        f"{indent}{STATIC}{key}: {format_value(value, depth)}"
                    )
        result = itertools.chain("{", lines, [closing_indent + "}"])
        return "\n".join(result)

    return walk(diff, 0)
