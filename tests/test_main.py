import argparse
import sys
import unittest

from main import create_parser, sort_imports, check_for_py_files


class TestSortImports(unittest.TestCase):
    def test_parser(self):
        """Check if create_parser() returns a parser object"""
        result = create_parser()
        self.assertIsInstance(
            result,
            argparse.ArgumentParser,
            "create_parser() function is not returning a parser object",
        )

    # def test_easy_sort_imports(self):
    #     """tests sorting imports functions"""
    #     args = ["test_file.py", "tests/test_directory_1"]
    #     result = sort_imports(args)
    #     # expected

    # def test_edge_case_sort_imports(self):
    #     """tests sorting imports functions"""
    #     args = ["edge_case_file.py", "tests/test_directory_2"]
    #     result = sort_imports(args)
    #     # expected

    def test_easy_check_for_py_files(self):
        """checks python file extenstions"""
        args = "tests/test_directory_1"
        result = check_for_py_files(args)
        expected = ["test_file_1.py"]
        self.assertEqual(result, expected)

    def test_difficult_check_for_py_files(self):
        """checks python file extenstions"""
        args = "tests/test_directory_2"
        result = check_for_py_files(args)
        expected = ["models.py", "forms.py", "test_file2.py"]
        self.assertEqual(result, expected)
