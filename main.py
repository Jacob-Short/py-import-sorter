import argparse
import os
import sys

# for python 3.8 and earlier
# from typing import List, Set, Dict, Tuple, Optional


exit_flag = False


def create_parser() -> argparse.ArgumentParser:
    """Returns an instance Parser"""
    parser = argparse.ArgumentParser(
        description="""Will connect to crypto socket
        from binance using symbol passed in
        """
    )

    parser.add_argument("dir", help="name of directory to sort python files")

    print(f"Parser:\n{type(parser)}")
    return parser


def sort_imports(py_file, dir) -> list:
    """will look at all .py files and sort all imports"""
    import_names = []
    with open(os.path.join(dir, py_file)) as f:
        # this is where the lines are being broken up
        all_lines = f.readlines()

        # TODO:
        # need to look at next iterations in list
        # until matching ')' is found
        for index, line in enumerate(all_lines):
            if line.strip().endswith("("):
                print(f"This is a edge case: [ {line} ]")

        sorted_import_names = sorted(
            [
                line
                for line in all_lines
                if line.startswith("import") or line.startswith("from")
            ]
        )

        # adding new line to give separation between import &&
            # non import lines
        sorted_import_names.append("\n")
        non_import_lines = [
            line
            for line in all_lines
            if not line.startswith("import") and not line.startswith("from")
        ]

        non_import_lines.append("\n")

        print(f"import lines:\n{sorted_import_names}")
        print(f"non import lines:\n{non_import_lines}")

        result = sorted_import_names + non_import_lines
        # print(f"End Result:\n{result}")

    with open(os.path.join(dir, py_file), "w") as wf:
        wf.writelines(result)

    # print(type(sorted_import_names))
    return sorted_import_names


def check_for_py_files(directory) -> list:
    """will look at all .py files and sort all imports"""
    full_path = os.path.abspath(directory)
    py_files = [file for file in os.listdir(full_path) if file.endswith(".py")]
    for file in py_files:
        print(f"Found a python file: [ {file} ], starting to sort now...")
        sort_imports(file, directory)
    print(type(py_files))
    return py_files


def main(args):
    """will look through all python files and sort imports"""

    parser = create_parser()
    ns = parser.parse_args(args)

    directory = ns.dir

    if not ns:
        parser.print_usage()

    while not exit_flag:
        try:
            check_for_py_files(directory)
            break
        except Exception as err:
            print(err)


if __name__ == "__main__":
    main(sys.argv[1:])
