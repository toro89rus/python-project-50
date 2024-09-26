import gendiff.diff_generator as diff_generator
import gendiff.parser as parser
from gendiff import generate_diff


def test_define_diff():
    expected = {
        "changed": {"timeout"},
        "unchanged": {"host"},
        "added": {"verbose"},
        "removed": {"follow", "proxy"},
    }
    # test JSON files
    file1 = parser.parse_file("tests/fixtures/flat1.json")
    file2 = parser.parse_file("tests/fixtures/flat2.json")

    assert diff_generator.define_diff(file1, file2) == expected

    # test YAML files
    file1 = parser.parse_file("tests/fixtures/flat1.yaml")
    file2 = parser.parse_file("tests/fixtures/flat2.yaml")
    assert diff_generator.define_diff(file1, file2)


def test_format_line():
    assert (
        diff_generator.format_line("host", "hexlet.io") == "    host: hexlet.io"
    )
    assert (
        diff_generator.format_line("host", "hexlet.io", "-")
        == "  - host: hexlet.io"
    )
    assert (
        diff_generator.format_line("host", "hexlet.io", "*")
        == "  * host: hexlet.io"
    )
    assert diff_generator.format_line("follow", False) == "    follow: false"


def test_generate_flat_diff_json():
    file1 = "tests/fixtures/flat1.json"
    file2 = "tests/fixtures/flat2.json"
    result_file = "tests/fixtures/result_flat_diff.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip(
            "\n"
        )


def test_generate_flat_diff_yaml():
    file1 = "tests/fixtures/flat1.yaml"
    file2 = "tests/fixtures/flat2.yaml"
    result_file = "tests/fixtures/result_flat_diff.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip(
            "\n"
        )


def test_generate_flat_diff_json_yaml():
    file1 = "tests/fixtures/flat1.json"
    file2 = "tests/fixtures/flat2.yaml"
    result_file = "tests/fixtures/result_flat_diff.txt"

    with open(result_file) as result:
        assert generate_diff(file1, file2) == result.read().strip("\n")
