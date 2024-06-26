import logging
import tkinter
from tkinter.constants import END

import customtkinter

import guest
import json_reader
import message


class GUI:

    def __init__(self, list_of_guests, list_of_companies, list_of_messages):
        self.list_of_guests = list_of_guests
        self.list_of_companies = list_of_companies
        self.list_of_messages = list_of_messages

        self.customtkinter = customtkinter

        self.root = customtkinter.CTk()
        self.root.geometry("1100x600")

        self.customtkinter.set_appearance_mode("dark")
        self.customtkinter.set_default_color_theme("blue")

        self.frame = customtkinter.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # widgets
        self.label = customtkinter.CTkLabel(self.root, text="Message Processor")
        self.label.pack(pady=12, padx=10)

        self.first_name_var = customtkinter.StringVar()

        self.first_name_label = customtkinter.CTkLabel(self.root, text="Guest First Name", bg_color="transparent")
        self.first_name_label.place(x=100, y=25)
        self.first_name_textfield = customtkinter.CTkEntry(self.root, textvariable=self.first_name_var)
        self.first_name_textfield.place(x=100, y=50)

        self.last_name_var = customtkinter.StringVar()

        self.last_name_label = customtkinter.CTkLabel(self.root, text="Guest Last Name")
        self.last_name_label.place(x=250, y=25)
        self.last_name_textfield = customtkinter.CTkEntry(self.root, textvariable=self.last_name_var)
        self.last_name_textfield.place(x=250, y=50)

        self.room_number_var = customtkinter.StringVar()

        self.room_number_label = customtkinter.CTkLabel(self.root, text="Room Number")
        self.room_number_label.place(x=100, y=100)
        self.room_number_textfield = customtkinter.CTkEntry(self.root, textvariable=self.room_number_var)
        self.room_number_textfield.place(x=100, y=125)

        self.message_var = customtkinter.StringVar()

        self.message_textfield = customtkinter.CTkTextbox(self.root, height=225, width=600, )
        self.message_textfield.place(x=100, y=180)

        self.message_template_var = customtkinter.StringVar()
        self.message_template_var.set("Select an option")

        self.message_template_label = customtkinter.CTkLabel(self.root, text="Message Template Selection")
        self.message_template_label.place(x=100, y=425)
        self.message_template_scrollbar = customtkinter.CTkOptionMenu(self.root,
                                                                      values=GUI.fill_message_template_list(self),
                                                                      variable=self.message_template_var,
                                                                      command=self.update_message_textfield
                                                                      )
        self.message_template_scrollbar.place(x=100, y=450)

        self.company_var = customtkinter.StringVar()
        self.company_var.set("Select a Company")

        self.company_scrollbar_label = customtkinter.CTkLabel(self.root, text="Company Options")
        self.company_scrollbar_label.place(x=800, y=25)
        self.company_scrollbar = customtkinter.CTkOptionMenu(self.root,
                                                             values=GUI.fill_company_list(self),
                                                             variable=self.company_var)
        self.company_scrollbar.place(x=800, y=50)

        self.guest_scrollbar_label = customtkinter.CTkLabel(self.root, text="Guest Selection")
        self.guest_scrollbar_label.place(x=800, y=100)
        self.guest_scrollbar = customtkinter.CTkOptionMenu(self.root,
                                                           values=GUI.fill_guest_list(self),
                                                           command=self.update_guest_info_textfield
                                                           )
        self.guest_scrollbar.place(x=800, y=125)

        self.send_button = customtkinter.CTkButton(self.root, text="Send Message", command=self.send_message)
        self.send_button.place(x=800, y=450)

        self.root.mainloop()

    def send_message(self):
        greeting = message.change_greeting()
        first_name = ""
        last_name = ""
        room_number = ""
        company = ""
        sending_message = True

        if self.first_name_var.get() == "":
            logging.error("You are missing the guest first name. Please enter a guest first name and try again.")
            sending_message = False
        else:
            first_name = self.first_name_var.get()

        if self.last_name_var.get() == "":
            logging.error("You are missing the guest last name. Please enter a guest last name and try again.")
            sending_message = False
        else:
            last_name = self.last_name_var.get()

        if self.room_number_var.get() == "":
            logging.error("You are missing the room number. Please enter a room number and try again.")
            sending_message = False
        else:
            room_number = self.room_number_var.get()

        if self.company_var.get() == "Select a Company":
            logging.error("Please select a company site and try again.")
            sending_message = False
        else:
            company = self.company_var.get()

        text = self.message_textfield.get("1.0", END)

        if sending_message:
            try:
                print(text.format(greeting=greeting,
                                  first_name=first_name,
                                  last_name=last_name,
                                  room_number=room_number,
                                  hotel=company))
            except KeyError as e:
                logging.error(f"{e} is an unknown variable in the message. Please try again.")

    def update_guest_info_textfield(self, text):
        room_number = ""

        for x in self.list_of_guests:
            if x.first_name + " " + x.last_name == text:
                room_number = x.room_number
                break

        self.first_name_textfield.delete(0, END)
        self.first_name_textfield.insert(0, text.split(" ")[0])
        self.last_name_textfield.delete(0, END)
        self.last_name_textfield.insert(0, text.split(" ")[1])
        self.room_number_textfield.delete(0, END)
        self.room_number_textfield.insert(0, room_number)

    def update_message_textfield(self, text):
        message_text = ""

        for x in self.list_of_messages:
            if x.get_message_type() == text:
                message_text = x.get_message_text()
                break

        self.message_textfield.delete("1.0", END)
        self.message_textfield.insert("1.0", message_text)

    def fill_guest_list(self):
        """
        Fills in the guest list dropdown
        :return: a list of guests names
        """

        list_of_names = []

        for x in self.list_of_guests:
            guest_name = x.get_first_name() + " " + x.get_last_name()
            list_of_names.append(guest_name)

        return list_of_names

    def fill_company_list(self):
        """
        Fills in the company list dropdown
        :return: a list of companies
        """

        list_of_company_names = []

        for x in self.list_of_companies:
            company_name = x.get_company_name()
            list_of_company_names.append(company_name)

        return list_of_company_names

    def fill_message_template_list(self):
        """
        Fills in the message template dropdown
        :return: a list of message template
        """

        list_of_message_template_types = []

        for x in self.list_of_messages:
            message_template_type = x.get_message_type()
            list_of_message_template_types.append(message_template_type)

        return list_of_message_template_types

    """
    def first_name_fill_message_textfield(self):

        text = self.first_name_var.get()
        new_message = ""

        for x in self.list_of_messages:
            x.set_first_name(text)
            new_message = x.create_message()

        self.message_textfield.delete("1.0", END)
        self.message_textfield.insert("1.0", new_message)

    def last_name_fill_message_textfield(self):

        text = self.last_name_var.get()
        new_message = ""

        for x in self.list_of_messages:
            x.set_last_name(text)
            new_message = x.create_message()

        self.message_textfield.delete("1.0", END)
        self.message_textfield.insert("1.0", new_message)
    """
