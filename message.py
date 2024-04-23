import re
from datetime import datetime


def check_time():
    """
    Checks the current time
    """

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return current_time


def change_greeting():
    """
        Change the greeting based on what time it is
        :return: the type of greeting to be used in the welcome message
        """

    hour_time = str(check_time()[0]) + str(check_time()[1])

    if 5 <= int(hour_time) < 12:
        return "Good morning,"
    elif 12 <= int(hour_time) < 17:
        return "Good afternoon,"
    elif 17 <= int(hour_time) < 21:
        return "Good evening,"
    else:
        return "Good night,"


class Message:

    def __init__(self, message_text, message_type):
        self.message_text = message_text
        self.message_type = message_type

    def get_message_text(self):
        return self.message_text

    def set_message_text(self, text):
        self.message_text = text

    def get_message_type(self):
        return self.message_type
