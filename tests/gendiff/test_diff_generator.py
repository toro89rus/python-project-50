import gendiff.diff_generator as diff_generator


def test_parse_json():
    file = "tests/fixtures/flat1.json"
    expected = "tests/fixtures/flat1_parsed.txt"
    with open(expected) as expected:
        assert diff_generator.parse_json(file) == {
            "follow": False,
            "host": "hexlet.io",
            "proxy": "123.234.53.22",
            "timeout": 50,
        }


def test_define_keys_diff():
    file1 = diff_generator.parse_json("tests/fixtures/flat1.json")
    file2 = diff_generator.parse_json("tests/fixtures/flat2.json")

    assert diff_generator.define_diff(file1, file2) == {
        "changed": {"timeout"},
        'unchanged': {"host"},
        "added": {"verbose"},
        "removed": {"follow", "proxy"},
    }


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


def test_generate_flat_diff():
    file1 = "tests/fixtures/flat1.json"
    file2 = "tests/fixtures/flat2.json"
    result_file = "tests/fixtures/result_flat_diff.txt"

    with open(result_file) as result:
        assert diff_generator.generate_diff(
            file1, file2
        ) == result.read().strip("\n")
