import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=argparse.FileType("r"))
    parser.add_argument("second_file", type=argparse.FileType("r"))
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output: stylish(default), plain, json",
        default="stylish",
    )
    args = parser.parse_args()
    return args.first_file.name, args.second_file.name, args.format
