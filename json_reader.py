import json
import re

import company
import guest
import message


class Json_reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.json_list = []

    def open_json_file(self):
        """
        Opens up a specified json file
        :return: a str of the contents of the file
        """

        if ".json" in self.file_name:
            file = open(self.file_name)
            data = json.load(file)
            file.close()
            self.json_list = data
        elif ".json" not in self.file_name:
            return "Your file could not be found"

    def create_list_of_guest(self):
        list_of_guest = []

        for x in self.json_list:
            first_name = parse_data("firstName", str(x))
            last_name = parse_data("lastName", str(x))
            room_number = parse_data("roomNumber", str(x))

            list_of_guest.append(guest.Guest(first_name, last_name, room_number))

        return list_of_guest

    def create_list_of_companies(self):
        list_of_companies = []

        for x in self.json_list:
            company_name = parse_data("company", str(x))
            company_id = parse_data("id", str(x))

            list_of_companies.append(company.Company(company_name, company_id))

        return list_of_companies

    def create_list_of_messages(self):
        list_of_messages = []

        for x in self.json_list:
            message_text = parse_data("message", str(x))
            message_type = parse_data("type", str(x))

            list_of_messages.append(message.Message(message_text, message_type))

        return list_of_messages


def parse_data(identifier, string):
    id_span = re.search(identifier, string)
    new_string = ""

    for index, char in enumerate(string[id_span.end():]):
        if char != ",":
            new_string = new_string + char
        else:
            break

    if new_string[-1] == "}":
        new_string = new_string[:-1]

    return re.sub("[':]", "", new_string).strip()
