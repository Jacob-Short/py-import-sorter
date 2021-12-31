import argparse
import os
import sys

# for python 3.8 and earlier
# from typing import List, Set, Dict, Tuple, Optional


def create_parser() -> argparse.ArgumentParser:
    """Returns an instance Parser"""
    parser = argparse.ArgumentParser(
        description="""args for directory to sort
        """
    )
    parser.add_argument("dir", help="name of directory to sort python files")
    return parser


def main(args):
    """will look through all python files and sort imports"""

    parser = create_parser()
    ns = parser.parse_args(args)

    directory = ns.dir

    if not ns:
        parser.print_usage()

    exit_flag = False

    while not exit_flag:
        try:
            py_files = check_for_py_files(directory)
            if len(py_files) > 1:
                for file_num, file in enumerate(py_files):
                    print(
                        f"#{file_num + 1} -- Found a python file: [ {file} ], starting to sort now..."
                    )
                    sort_imports(file, directory)
                exit_flag = True
            else:
                print(f"There are no python files within {directory}")
                break
        except FileNotFoundError as err:
            print(f"'{directory}' does not exist. The asolute path is required.")
            break
        except Exception as err:
            # TODO:
            # set up logging for when unexpected things go wrong.
            # can later add them to exceptions.
            print(err)
            break


def check_for_py_files(directory: str) -> list:
    """takes in abs path of directory and will look at all .py files
    and sort all imports
    """
    full_path = os.path.abspath(directory)
    py_files = [file for file in os.listdir(full_path) if file.endswith(".py")]
    return py_files


def multi_line_checker(lines: list) -> list:
    """takes in a list of lines and checks for multi
    line import statements
    Ex:
    from messaging.forms import (
        Messaging,
        SendMessage,
        DeleteMessage
    )
    """
    # TODO:
    # refactor using regex
    multi_line_imports = []
    multi_line = False

    for index, line in enumerate(lines):
        if line.strip().startswith("from") and line.strip().endswith("("):
            print(f"This is a edge case: [ {line} ]")
            multi_line_imports.append(line)
            multi_line = True
        elif line.strip().endswith(")") and multi_line:
            multi_line_imports.append(line)
            multi_line = False
        elif multi_line:
            multi_line_imports.append(line)
    print(f"multi-line imports:\n{multi_line_imports}")
    """
    this section is to check if there are any multi-line import statements
    and if so then to sort them
    """
    if len(multi_line_imports) > 1:
        sorted_multi_line_imports = sorted([line for line in multi_line_imports[1:-1]])
        print(f"sorted edge case lines:\n{sorted_multi_line_imports}")
        sorted_multi_line_imports.insert(0, multi_line_imports[0])
        sorted_multi_line_imports.append(multi_line_imports[-1])
        print(f"FINAL RESULT OF sorted edge case lines:\n{sorted_multi_line_imports}")
        return sorted_multi_line_imports
    else:
        return multi_line_imports


def sort_imports(py_file: str, dir: str) -> None:
    """will look at all .py files and sort all imports"""

    import_names = []
    with open(os.path.join(dir, py_file)) as f:
        all_lines = f.readlines()

        """
        this section is to account for multi line import statements
        EX:
        from user_account.forms import (
            CreateProfileForm,
            LoginForm,
            RegisterForm,
        )
        """

        multi_line_imports = multi_line_checker(all_lines)

        sorted_import_names = sorted(
            [
                line
                for line in all_lines
                if line.startswith("import")
                or line.startswith("from")
                and line not in multi_line_imports
            ]
        )

        """
        doing this to create new line between reg imports & from
        import statements
        Ex:
            Before:

                import argparse
                from django import widgets
                import time
                from django import forms
            After:
            
                from django import forms
                from django import widgets

                import argarse
                importtime
        """
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
            and line not in multi_line_imports
        ]
        non_import_lines.append("\n")

        non_import_lines.append("\n")

        print(f"import lines:\n{sorted_import_names}")
        print(f"non import lines:\n{non_import_lines}")

        result = sorted_import_names + multi_line_imports + non_import_lines

    with open(os.path.join(dir, py_file), "w") as wf:
        wf.writelines(result)

        # TODO:
        # before closing the file -- can run flake8 / black

    return None


if __name__ == "__main__":
    main(sys.argv[1:])
