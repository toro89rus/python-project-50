import json

import yaml


def parse_file(filename):
    if filename.endswith(".json"):
        data = parse_json(filename)
    elif filename.endswith((".yaml", ".yml")):
        data = parse_yaml(filename)
    return data


def parse_json(filename):
    data = json.load(open(filename))
    return data


def parse_yaml(filename):
    data = yaml.load(open(filename), Loader=yaml.Loader)
    return data
