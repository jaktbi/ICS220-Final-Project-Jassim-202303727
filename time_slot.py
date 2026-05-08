# TimeSlot class represents an available booking period
class TimeSlot:

    # Constructor to initialize time slot object
    def __init__(self, slot_id, date, start_time,
                 end_time, is_booked, reserved_count):

        # Store time slot attributes as private
        self.__slot_id = slot_id
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__is_booked = is_booked
        self.__reserved_count = reserved_count

    # Getter method to return slot ID
    def get_slot_id(self):
        return self.__slot_id

    # Getter method to return date
    def get_date(self):
        return self.__date

    # Getter method to return start time
    def get_start_time(self):
        return self.__start_time

    # Getter method to return end time
    def get_end_time(self):
        return self.__end_time

    # Getter method to return booking status
    def get_is_booked(self):
        return self.__is_booked

    # Getter method to return reserved count
    def get_reserved_count(self):
        return self.__reserved_count

    # Setter method to update slot ID
    def set_slot_id(self, slot_id):
        self.__slot_id = slot_id

    # Setter method to update date
    def set_date(self, date):
        self.__date = date

    # Setter method to update start time
    def set_start_time(self, start_time):
        self.__start_time = start_time

    # Setter method to update end time
    def set_end_time(self, end_time):
        self.__end_time = end_time

    # Setter method to update booking status
    def set_is_booked(self, is_booked):
        self.__is_booked = is_booked

    # Setter method to update reserved count
    def set_reserved_count(self, reserved_count):
        self.__reserved_count = reserved_count

    # Method to check if the slot is available
    def check_slot_availability(self):
        return not self.__is_booked

    # Method to reserve the slot
    def reserve_slot(self):
        self.__is_booked = True
        self.__reserved_count += 1

    # Method to release the slot
    def release_slot(self):
        self.__is_booked = False

    # Method to display slot details
    def display_slot_details(self):
        return (f"Date: {self.__date} | "
                f"Time: {self.__start_time} - {self.__end_time}")

    # String method to display time slot clearly
    def __str__(self):
        return self.display_slot_details()