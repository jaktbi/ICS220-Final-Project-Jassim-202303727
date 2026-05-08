# AccessType class represents the access level of a user
class AccessType:

    # Constructor to create an access type object
    def __init__(self, access_name, allowed_facility_types, priority_level, description):
        self.__access_name = access_name
        self.__allowed_facility_types = allowed_facility_types
        self.__priority_level = priority_level
        self.__description = description

    # Return access name
    def get_access_name(self):
        return self.__access_name

    # Return allowed facility types
    def get_allowed_facility_types(self):
        return self.__allowed_facility_types

    # Return priority level
    def get_priority_level(self):
        return self.__priority_level

    # Return description
    def get_description(self):
        return self.__description

    # Check if facility type is allowed
    def can_book_facility_type(self, facility_type):
        return facility_type in self.__allowed_facility_types

    # Return access details
    def get_access_details(self):
        return f"{self.__access_name} Access - {self.__description}"

    # Display access type clearly
    def __str__(self):
        return self.get_access_details()