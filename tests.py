import unittest

import json_reader


class Test(unittest.TestCase):

    def test_incorrect_file_name(self):
        self.assertEqual(json_reader.Json_reader("INCORRECT_FILE").open_json_file(), "Your file could not be found")

    def test_non_json_file(self):
        self.assertEqual(json_reader.Json_reader("json_files/non_json_file").open_json_file(), "Your file could not be found")

    def test_data_loads(self):
        data = json_reader.Json_reader("json_files/Guests.json")
        data.open_json_file()
        self.assertNotEqual(data.create_list_of_guest(), "")

