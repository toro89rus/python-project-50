#!/usr/bin/env python3

import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=argparse.FileType("r"))
    parser.add_argument("second_file", type=argparse.FileType("r"))
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    file1, file2 = args.first_file.name, args.second_file.name
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == "__main__":
    main()
