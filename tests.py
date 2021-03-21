# -*- coding: utf-8 -*-
import unittest
from model import Output

class OutputTestCase(unittest.TestCase):

    def test_output_items(self):
        res = Output.items()
        test_dict = ["date", "sku"]
        self.assertIn(test_dict, res)

    def test_output_items(self):
        res = Output.items()
        test_dict = ["date", "sku"]
        self.assertIn(test_dict, res)

if __name__ == '__main__':
    unittest.main()