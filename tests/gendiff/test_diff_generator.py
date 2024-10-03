import gendiff.diff_generator as diff_generator
import gendiff.parser as parser
from gendiff import generate_diff


def test_define_diff():
    expected = {
        "follow": {"status": "removed", "value": False},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "proxy": {"status": "removed", "value": "123.234.53.22"},
        "timeout": {"status": "changed", "value": (50, 20)},
        "verbose": {"status": "added", "value": True},
    }
    # test JSON files
    file1 = parser.parse_file("tests/fixtures/flat1.json")
    file2 = parser.parse_file("tests/fixtures/flat2.json")

    assert diff_generator.define_diff(file1, file2) == expected

    # test YAML files
    file1 = parser.parse_file("tests/fixtures/flat1.yaml")
    file2 = parser.parse_file("tests/fixtures/flat2.yaml")
    assert diff_generator.define_diff(file1, file2)


def test_generate_flat_diff_json():
    file1 = "tests/fixtures/flat1.json"
    file2 = "tests/fixtures/flat2.json"
    result_file = "tests/fixtures/result_flat_diff_stylish.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")


def test_generate_flat_diff_yaml():
    file1 = "tests/fixtures/flat1.yaml"
    file2 = "tests/fixtures/flat2.yaml"
    result_file = "tests/fixtures/result_flat_diff_stylish.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")


def test_generate_flat_diff_json_yaml():
    file1 = "tests/fixtures/flat1.json"
    file2 = "tests/fixtures/flat2.yaml"
    result_file = "tests/fixtures/result_flat_diff_stylish.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")


def test_generate_nested_diff_json():
    file1 = "tests/fixtures/nested1.json"
    file2 = "tests/fixtures/nested2.json"
    result_file = "tests/fixtures/result_nested_diff_stylish.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")


def test_generate_nested_diff_yaml_plain():
    file1 = "tests/fixtures/nested1.yaml"
    file2 = "tests/fixtures/nested2.yaml"
    result_file = "tests/fixtures/result_nested_diff_plain.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2, "plain") == result.read().strip("\n")


def test_generate_nested_diff_json_stylish():
    file1 = "tests/fixtures/nested1.json"
    file2 = "tests/fixtures/nested2.json"
    result_file = "tests/fixtures/result_nested_diff_stylish.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")
