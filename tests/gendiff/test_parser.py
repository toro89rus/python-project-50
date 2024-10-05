import gendiff.parser as parser

expected = {
    "follow": False,
    "host": "hexlet.io",
    "proxy": "123.234.53.22",
    "timeout": 50,
}


def test_parse_json():
    file = "tests/fixtures/flat/flat1.json"
    assert parser.parse_content(file) == expected


def test_parse_yaml():
    yaml_file = "tests/fixtures/flat/flat1.yaml"
    yml_file = "tests/fixtures/flat/flat1.yml"
    assert parser.parse_content(yaml_file) == expected
    assert parser.parse_content(yml_file) == expected
