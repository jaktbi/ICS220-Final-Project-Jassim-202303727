# Import pickle library to save and load objects in binary files
import pickle


# DataManager class handles all Pickle file operations
class DataManager:

    # Constructor to initialize file names
    def __init__(self):
        self.__users_file = "users.pkl"  # File used to store user objects
        self.__facilities_file = "facilities.pkl"  # File used to store facility objects
        self.__bookings_file = "bookings.pkl"  # File used to store booking objects
        self.__confirmations_file = "confirmations.pkl"  # File used to store confirmation objects

    # Method to save users list into Pickle file
    def save_users(self, users):
        with open(self.__users_file, "wb") as file:  # Open users file in binary write mode
            pickle.dump(users, file)  # Save users list into file

    # Method to load users list from Pickle file
    def load_users(self):
        try:
            with open(self.__users_file, "rb") as file:  # Open users file in binary read mode
                return pickle.load(file)  # Return loaded users list
        except FileNotFoundError:
            return []  # Return empty list if file does not exist yet

    # Method to save facilities list into Pickle file
    def save_facilities(self, facilities):
        with open(self.__facilities_file, "wb") as file:  # Open facilities file in binary write mode
            pickle.dump(facilities, file)  # Save facilities list into file

    # Method to load facilities list from Pickle file
    def load_facilities(self):
        try:
            with open(self.__facilities_file, "rb") as file:  # Open facilities file in binary read mode
                return pickle.load(file)  # Return loaded facilities list
        except FileNotFoundError:
            return []  # Return empty list if file does not exist yet

    # Method to save bookings list into Pickle file
    def save_bookings(self, bookings):
        with open(self.__bookings_file, "wb") as file:  # Open bookings file in binary write mode
            pickle.dump(bookings, file)  # Save bookings list into file

    # Method to load bookings list from Pickle file
    def load_bookings(self):
        try:
            with open(self.__bookings_file, "rb") as file:  # Open bookings file in binary read mode
                return pickle.load(file)  # Return loaded bookings list
        except FileNotFoundError:
            return []  # Return empty list if file does not exist yet

    # Method to save confirmations list into Pickle file
    def save_confirmations(self, confirmations):
        with open(self.__confirmations_file, "wb") as file:  # Open confirmations file in binary write mode
            pickle.dump(confirmations, file)  # Save confirmations list into file

    # Method to load confirmations list from Pickle file
    def load_confirmations(self):
        try:
            with open(self.__confirmations_file, "rb") as file:  # Open confirmations file in binary read mode
                return pickle.load(file)  # Return loaded confirmations list
        except FileNotFoundError:
            return []  # Return empty list if file does not exist yet