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

    def test_sort_imports(self):
        """tests sorting imports functions"""
        pass

    def test_check_for_py_files(self):
        """checks python file extenstions"""
        args = "tests/directory_with_py_files"
        result = check_for_py_files(args)
        expected = ["target_file.py", "forms.py"]
        self.assertEquals(result, expected)
