# Import the AccessType class so it can be used inside the User class
from access_type import AccessType

# User class represents a normal system user
class User:

    # Constructor to initialize a user object
    def __init__(self, user_id, name, email, password, phone_number, access_type):
        self.__user_id = user_id  # Store user ID as private
        self.__name = name  # Store user name as private
        self.__email = email  # Store email as private
        self.__password = password  # Store password as private
        self.__phone_number = phone_number  # Store phone number as private
        self.__access_type = access_type  # Store AccessType object as private
        self.__booking_history = []  # Store booking history as private list

    # Getter method to return user ID
    def get_user_id(self):
        return self.__user_id  # Return user ID

    # Getter method to return name
    def get_name(self):
        return self.__name  # Return user name

    # Getter method to return email
    def get_email(self):
        return self.__email  # Return email

    # Getter method to return password
    def get_password(self):
        return self.__password  # Return password

    # Getter method to return phone number
    def get_phone_number(self):
        return self.__phone_number  # Return phone number

    # Getter method to return access type
    def get_access_type(self):
        return self.__access_type  # Return AccessType object

    # Getter method to return booking history
    def get_booking_history(self):
        return self.__booking_history  # Return booking history list

    # Setter method to update user ID
    def set_user_id(self, user_id):
        self.__user_id = user_id  # Update user ID

    # Setter method to update name
    def set_name(self, name):
        self.__name = name  # Update user name

    # Setter method to update email
    def set_email(self, email):
        self.__email = email  # Update email

    # Setter method to update password
    def set_password(self, password):
        self.__password = password  # Update password

    # Setter method to update phone number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number  # Update phone number

    # Setter method to update access type
    def set_access_type(self, access_type):
        self.__access_type = access_type  # Update access type

    # Method to create a new account
    def create_account(self):
        # This method should create and save a new user account
        pass

    # Method to log into the system
    def login(self):
        # This method should validate login credentials
        pass

    # Method to update user profile details
    def update_profile(self):
        # This method should update user information
        pass

    # Method to display booking history
    def view_booking_history(self):
        # This method should display all user bookings
        pass

    # Method to request a booking
    def request_booking(self):
        # This method should allow the user to request a booking
        pass

    # Method to cancel a booking
    def cancel_booking(self):
        # This method should cancel an existing booking
        pass

    # Method to add a booking object to booking history
    def add_booking_to_history(self, booking):
        self.__booking_history.append(booking)  # Add booking to booking history list

    # String method to display user details clearly
    def __str__(self):
        return f"User ID: {self.__user_id}, Name: {self.__name}, Email: {self.__email}"
