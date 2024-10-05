from gendiff.formatters import json_format, plain, stylish


def format_diff(diff, format):
    match format:
        case "stylish":
            formated_diff = stylish.format_diff(diff)
        case "plain":
            formated_diff = plain.format_diff(diff)
        case "json":
            formated_diff = json_format.format_diff(diff)
        case _:
            raise ValueError(
                f"Unsopported format: {format}."
                f" Please choose stylish, plain or json"
            )

    return formated_diff
