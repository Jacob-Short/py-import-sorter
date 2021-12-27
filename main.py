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

        # temp placeholder for edge case lines
        multi_line = False
        edge_case_lines = []

        # this takes a lot of time. lets look back into this later
        # for efficiency
        for index, line in enumerate(all_lines):
            if line.strip().endswith(")"):
                edge_case_lines.append(line)
                multi_line = False
            if multi_line:
                edge_case_lines.append(line)
            if line.strip().endswith("("):
                print(f"This is a edge case: [ {line} ]")
                edge_case_lines.append(line)
                multi_line = True

        edge_case_lines.append('\n')

        print(f"edge cases:\n{edge_case_lines}")

        # TODO:
            # edge cases need to be sorted

        # sort_edge_cases(all[index:])
        # pass the rest of the list && line num
        # to create a edge_case_lists
        # then can append them all after

        # OR

        # can create boolean multi_line = False
        # then can set to true when find the opening '('
        # then will append all future iterations until
        # finding the closing ')' then can set back to False

        # TODO:
        # will need to remove all edge case lines from both
        # sorted import && non import lists
        sorted_import_names = sorted(
            [
                line
                for line in all_lines
                if line.startswith("import")
                or line.startswith("from")
                and line not in edge_case_lines
            ]
        )

        # TODO:
        # add new line in between reg imports & 'from' imports

        for ind, line in enumerate(sorted_import_names):
            if line.startswith("import"):
                sorted_import_names.insert(ind, "\n")
                break

        sorted_import_names.append("\n")
        non_import_lines = [
            line
            for line in all_lines
            if not line.startswith("import")
            and not line.startswith("from")
            and line not in edge_case_lines
        ]
        non_import_lines.append("\n")

        print(f"import lines:\n{sorted_import_names}")
        print(f"non import lines:\n{non_import_lines}")

        result = sorted_import_names + edge_case_lines + non_import_lines
        # print(f"End Result:\n{result}")

    with open(os.path.join(dir, py_file), "w") as wf:
        wf.writelines(result)

    # print(type(sorted_import_names))
    return sorted_import_names


def sort_edge_cases(remaining_lines) -> list:
    """will append next iterations of lines with
    ' from pypy import (
        foo,
        bar,
    '
    )
    """
    for line in remaining_lines:
        print(line)


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
