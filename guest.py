class Guest:

    def __init__(self, first_name, last_name, room_number):
        self.first_name = first_name
        self.last_name = last_name
        self.room_number = room_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_room_number(self):
        return self.room_number

