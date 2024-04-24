import json_reader
import message
import GUI

if __name__ == '__main__':

    list_of_companies = json_reader.Json_reader("json_files/Companies.json")
    list_of_companies.open_json_file()

    list_of_messages = json_reader.Json_reader("json_files/Messages.json")
    list_of_messages.open_json_file()

    list_of_guests = json_reader.Json_reader("json_files/Guests.json")
    list_of_guests.open_json_file()

    GUI.GUI(list_of_guests.create_list_of_guest(),
            list_of_companies.create_list_of_companies(),
            list_of_messages.create_list_of_messages())
