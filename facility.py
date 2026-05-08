# Facility class represents a campus facility
class Facility:

    # Constructor to initialize facility object
    def __init__(self, facility_id, facility_name, facility_type,
                 capacity, booking_fee, availability_status):

        # Store facility attributes as private
        self.__facility_id = facility_id
        self.__facility_name = facility_name
        self.__facility_type = facility_type
        self.__capacity = capacity
        self.__booking_fee = booking_fee
        self.__availability_status = availability_status

        # Store all related time slots in a list
        self.__time_slots = []

    # Getter method to return facility ID
    def get_facility_id(self):
        return self.__facility_id

    # Getter method to return facility name
    def get_facility_name(self):
        return self.__facility_name

    # Getter method to return facility type
    def get_facility_type(self):
        return self.__facility_type

    # Getter method to return facility capacity
    def get_capacity(self):
        return self.__capacity

    # Getter method to return booking fee
    def get_booking_fee(self):
        return self.__booking_fee

    # Getter method to return availability status
    def get_availability_status(self):
        return self.__availability_status

    # Getter method to return all time slots
    def get_time_slots(self):
        return self.__time_slots

    # Setter method to update facility ID
    def set_facility_id(self, facility_id):
        self.__facility_id = facility_id

    # Setter method to update facility name
    def set_facility_name(self, facility_name):
        self.__facility_name = facility_name

    # Setter method to update facility type
    def set_facility_type(self, facility_type):
        self.__facility_type = facility_type

    # Setter method to update facility capacity
    def set_capacity(self, capacity):
        self.__capacity = capacity

    # Setter method to update booking fee
    def set_booking_fee(self, booking_fee):
        self.__booking_fee = booking_fee

    # Setter method to update availability status
    def set_availability_status(self, availability_status):
        self.__availability_status = availability_status

    # Method to display facility details
    def display_facility_details(self):
        return (f"Facility: {self.__facility_name} | "
                f"Type: {self.__facility_type} | "
                f"Capacity: {self.__capacity}")

    # Method to check facility availability
    def check_availability(self):
        return self.__availability_status

    # Method to add a time slot to the facility
    def add_time_slot(self, time_slot):
        self.__time_slots.append(time_slot)

    # Method to remove a time slot from the facility
    def remove_time_slot(self, time_slot):
        if time_slot in self.__time_slots:
            self.__time_slots.remove(time_slot)

    # Method to update facility fee
    def update_facility_fee(self, new_fee):
        self.__booking_fee = new_fee

    # String method to display facility clearly
    def __str__(self):
        return f"{self.__facility_name} ({self.__facility_type})"