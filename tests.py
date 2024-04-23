import unittest

import json_reader


class Test(unittest.TestCase):

    def test_incorrect_file_name(self):
        self.assertEqual(json_reader.open_json_file("INCORRECT_FILE"), "Your file could not be found")

    def test_non_json_file(self):
        self.assertEqual(json_reader.open_json_file("json_files/non_json_file"), "Your file could not be found")
