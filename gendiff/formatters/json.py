import json


def format_diff(diff):
    return json.dumps(diff, sort_keys=True)
