import json

import yaml

import os.path


def get_file_extension(path):
    return os.path.splitext(path)[1][1:]


def get_file_content(path):
    with open(path) as file:
        content = file.read()
    return content


def parse(content, format):
    if format == "json":
        return json.loads(content)
    elif format in ("yaml", "yml"):
        return yaml.load(content, Loader=yaml.Loader)
    raise TypeError(f"Unsupported file format {format}")


def parse_content(filepath):
    content = get_file_content(filepath)
    format = get_file_extension(filepath)
    return parse(content, format)
