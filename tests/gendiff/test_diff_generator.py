import pytest

from gendiff import generate_diff

fixtures_paths = [
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_stylish.txt",
        "stylish"
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_stylish.txt",
        "stylish"
    ),
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_stylish.txt",
        "stylish"
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_stylish.txt",
        "stylish"
    ),
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_plain.txt",
        "plain"
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_plain.txt",
        "plain"
    ),
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_plain.txt",
        "plain"
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_plain.txt",
        "plain"
    ),
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_json.txt",
        "json"
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_json.txt",
        "json"
    ),
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_json.txt",
        "json"
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_json.txt",
        "json"
    ),
]


@pytest.mark.parametrize("file1, file2, result_file, diff_format", fixtures_paths)
def test_generate_diff(file1, file2, result_file, diff_format):
    formatted_diff = generate_diff(file1, file2, diff_format)
    with open(result_file) as result:
        expected = result.read()
    assert formatted_diff == expected
