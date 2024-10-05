import itertools

ADDED_PREFIX = "+ "
REMOVED_PREFIX = "- "
UNCHANGED_PREFIX = "  "
NESTED_PREFIX = "  "
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
            line = (f"{indent}{NESTED_PREFIX}{key}: "
                    f"{format_value(nested_value, depth)}")
            lines.append(line)
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
                    nested_line = (f"{indent}{NESTED_PREFIX}{key}: "
                                   f"{walk(value, depth + 1)}")
                    lines.append(nested_line)
                case "removed":
                    removed_line = (f"{indent}{REMOVED_PREFIX}{key}: "
                                    f"{format_value(value, depth)}")
                    lines.append(removed_line)
                case "added":
                    added_line = (f"{indent}{ADDED_PREFIX}{key}: "
                                  f"{format_value(value, depth)}")
                    lines.append(added_line)
                case "changed":
                    old_value, new_value = value
                    old_line = (f"{indent}{REMOVED_PREFIX}{key}: "
                                f"{format_value(old_value, depth)}")
                    new_line = (f"{indent}{ADDED_PREFIX}{key}: "
                                f"{format_value(new_value, depth)}")
                    lines.append(old_line)
                    lines.append(new_line)
                case "unchanged":
                    unchanged_line = (f"{indent}{UNCHANGED_PREFIX}{key}: "
                                      f"{format_value(value, depth)}")
                    lines.append(unchanged_line)
        result = itertools.chain("{", lines, [closing_indent + "}"])
        return "\n".join(result)

    return walk(diff, 0)
