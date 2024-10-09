#!/usr/bin/env python3

from gendiff.cli_parser import get_args

from gendiff import generate_diff


def main():
    file1, file2, format_name = get_args()
    diff = generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == "__main__":
    main()
