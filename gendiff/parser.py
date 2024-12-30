import json

import yaml

import os.path

import pathlib


def get_file_extension(filepath):
    path = pathlib.Path(filepath)
    return path.suffix.lower()


def get_file_content(filepath):
    with open(filepath) as file:
        content = file.read()
    return content


def parse(content, format):
    if format == ".json":
        return json.loads(content)
    elif format in (".yaml", ".yml"):
        return yaml.load(content, Loader=yaml.Loader)
    raise TypeError(f"Unsupported file format {format}")


def parse_content(filepath):
    content = get_file_content(filepath)
    format = get_file_extension(filepath)
    return parse(content, format)
