import argparse
import logging
import os
import signal
import sys
import time


exit_flag = False


def create_parser():
    """Returns an instance Parser"""
    parser = argparse.ArgumentParser(
        description="""Will connect to crypto socket
        from binance using symbol passed in
        """
    )

    parser.add_argument("dir", help="name of directory to sort python files")

    return parser


def sort_imports(py_file, dir):
    """will look at all .py files and sort all imports"""
    import_names = []
    with open(os.path.join(dir, py_file)) as f:
        list_of_lines = f.readlines()
        print(list_of_lines)

        # TODO:
        # create list of import

        import_names = sorted(
            [line for line in list_of_lines if line.startswith("import")]
        )
        list_of_lines = [
            line for line in list_of_lines if not line.startswith("import")
        ]

        result = import_names + list_of_lines
        # list_of_lines.insert(0, import_names)

        # print(f"Import Names:\n{import_names}")
        print(f"End Result:\n{result}")

    with open(os.path.join(dir, py_file), "w") as wf:
        wf.writelines(result)


def check_for_py_files(directory):
    """will look at all .py files and sort all imports"""
    full_path = os.path.abspath(directory)
    py_files = [file for file in os.listdir(full_path) if file.endswith(".py")]
    for file in py_files:
        sort_imports(file, directory)


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
