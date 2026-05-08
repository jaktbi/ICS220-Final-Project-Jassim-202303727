# Import the User class so Administrator can inherit from it
from user import User


# Administrator class inherits from User
class Administrator(User):

    # Constructor to initialize administrator object
    def __init__(self, user_id, name, email, password, phone_number,
                 access_type, admin_id, department, role):

        # Call parent constructor from User class
        super().__init__(user_id, name, email, password,
                         phone_number, access_type)

        # Store administrator-specific attributes as private
        self.__admin_id = admin_id
        self.__department = department
        self.__role = role

    # Getter method to return administrator ID
    def get_admin_id(self):
        return self.__admin_id

    # Getter method to return department
    def get_department(self):
        return self.__department

    # Getter method to return role
    def get_role(self):
        return self.__role

    # Setter method to update administrator ID
    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id

    # Setter method to update department
    def set_department(self, department):
        self.__department = department

    # Setter method to update role
    def set_role(self, role):
        self.__role = role

    # Method to monitor daily bookings
    def monitor_daily_bookings(self):
        # This method should display daily booking activity
        pass

    # Method to update facility availability
    def update_facility_availability(self):
        # This method should update available facilities and time slots
        pass

    # Method to track facility usage
    def track_facility_usage(self):
        # This method should monitor facility usage statistics
        pass

    # Method to upgrade user access
    def upgrade_user_access(self):
        # This method should change a user's access type
        pass

    # Method to view facility status
    def view_facility_status(self):
        # This method should display current facility status
        pass

    # String method to display administrator details clearly
    def __str__(self):
        return f"Administrator: {self.get_name()} | Department: {self.__department}"