import itertools

NEW = "+ "
OLD = "- "
STATIC = "  "
INDENT_SIZE = 4
INDENT_SYMBOL = " "


def get_indents(depth, separator=INDENT_SYMBOL):
    opening_indent_size = depth * INDENT_SIZE + 2
    opening_indent = separator * opening_indent_size
    closing_indent_size = depth * 4
    closing_indent = separator * closing_indent_size
    return (opening_indent, closing_indent)


def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        lines = []
        depth += 1
        for key, nested_value in value.items():
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
