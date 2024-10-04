import json

import yaml


def parse_file(filename):
    if filename.endswith(".json"):
        data = parse_json(filename)
    elif filename.endswith((".yaml", ".yml")):
        data = parse_yaml(filename)
    return data


def parse_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


def parse_yaml(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.Loader)
    return data
