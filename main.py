import json_reader
import message
import GUI

if __name__ == '__main__':

    list_of_guests = json_reader.create_list_of_guest(json_reader.open_json_file("json_files/Guests.json"))
    list_of_companies = json_reader.create_list_of_companies(json_reader.open_json_file("json_files/Companies.json"))
    list_of_messages = json_reader.create_list_of_messages(json_reader.open_json_file("json_files/Messages.json"))

    GUI.GUI(list_of_guests, list_of_companies, list_of_messages)
