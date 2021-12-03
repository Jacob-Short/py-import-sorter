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
