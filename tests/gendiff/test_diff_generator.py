import json

import pytest

from gendiff import generate_diff

test_flat_stylish = [
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_stylish.txt",
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_stylish.txt",
    ),
]


test_flat_plain = [
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_plain.txt",
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_plain.txt",
    ),
]

test_flat_json = [
    (
        "tests/fixtures/flat/flat1.json",
        "tests/fixtures/flat/flat2.json",
        "tests/fixtures/result/result_flat_json.json",
    ),
    (
        "tests/fixtures/flat/flat1.yaml",
        "tests/fixtures/flat/flat2.yaml",
        "tests/fixtures/result/result_flat_json.json",
    ),
]

test_nested_stylish = [
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_stylish.txt",
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_stylish.txt",
    ),
]

test_nested_plain = [
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_plain.txt",
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_plain.txt",
    ),
]


test_nested_json = [
    (
        "tests/fixtures/nested/nested1.json",
        "tests/fixtures/nested/nested2.json",
        "tests/fixtures/result/result_nested_json.json",
    ),
    (
        "tests/fixtures/nested/nested1.yaml",
        "tests/fixtures/nested/nested2.yaml",
        "tests/fixtures/result/result_nested_json.json",
    ),
]


@pytest.mark.parametrize("file1, file2, result_file", test_flat_stylish)
def test_generate_diff_flat_stylish(file1, file2, result_file):
    formatted_diff = generate_diff(file1, file2)
    with open(result_file) as result:
        expected = result.read().strip("\n")
    assert formatted_diff == expected, "Flat stylish test failed"


@pytest.mark.parametrize("file1, file2, result_file", test_flat_plain)
def test_generate_diff_flat_plain(file1, file2, result_file):
    formatted_diff = generate_diff(file1, file2, "plain")
    with open(result_file) as result:
        expected = result.read().strip("\n")
    assert formatted_diff == expected, "Flat plain test failed"


@pytest.mark.parametrize("file1, file2, result_file", test_flat_json)
def test_generate_diff_flat_json(file1, file2, result_file):
    formatted_diff = json.loads(generate_diff(file1, file2, "json"))
    with open(result_file) as result:
        expected = json.load(result)
    assert formatted_diff == expected, "Flat json test failed"


@pytest.mark.parametrize("file1, file2, result_file", test_nested_stylish)
def test_generate_diff_nested_stylish(file1, file2, result_file):
    formatted_diff = generate_diff(file1, file2)
    with open(result_file) as result:
        expected = result.read().strip("\n")
    assert formatted_diff == expected, "Nested stylish test failed"


@pytest.mark.parametrize("file1, file2, result_file", test_nested_plain)
def test_generate_diff_nested_plain(file1, file2, result_file):
    formatted_diff = generate_diff(file1, file2, "plain")
    with open(result_file) as result:
        expected = result.read().strip("\n")
    assert formatted_diff == expected, "Nested plain test failed"


@pytest.mark.parametrize("file1, file2, result_file", test_nested_json)
def test_generate_diff_nested_json(file1, file2, result_file):
    formatted_diff = json.loads(generate_diff(file1, file2, "json"))
    with open(result_file) as result:
        expected = json.load(result)
    assert formatted_diff == expected, "Nested json test failed"
