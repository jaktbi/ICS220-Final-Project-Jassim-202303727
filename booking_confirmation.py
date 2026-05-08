# BookingConfirmation class represents the final booking confirmation
class BookingConfirmation:

    # Constructor to initialize confirmation object
    def __init__(self, confirmation_id, generated_date,
                 booking_details, confirmed_cost):

        # Store confirmation attributes as private
        self.__confirmation_id = confirmation_id
        self.__generated_date = generated_date
        self.__booking_details = booking_details
        self.__confirmed_cost = confirmed_cost

    # Getter method to return confirmation ID
    def get_confirmation_id(self):
        return self.__confirmation_id

    # Getter method to return generated date
    def get_generated_date(self):
        return self.__generated_date

    # Getter method to return booking details
    def get_booking_details(self):
        return self.__booking_details

    # Getter method to return confirmed cost
    def get_confirmed_cost(self):
        return self.__confirmed_cost

    # Setter method to update confirmation ID
    def set_confirmation_id(self, confirmation_id):
        self.__confirmation_id = confirmation_id

    # Setter method to update generated date
    def set_generated_date(self, generated_date):
        self.__generated_date = generated_date

    # Setter method to update booking details
    def set_booking_details(self, booking_details):
        self.__booking_details = booking_details

    # Setter method to update confirmed cost
    def set_confirmed_cost(self, confirmed_cost):
        self.__confirmed_cost = confirmed_cost

    # Method to generate confirmation details
    def generate_confirmation(self):
        return (f"Confirmation ID: {self.__confirmation_id}\n"
                f"Generated Date: {self.__generated_date}\n"
                f"Booking Details: {self.__booking_details}\n"
                f"Confirmed Cost: AED {self.__confirmed_cost}")

    # Method to display confirmation details
    def display_confirmation(self):
        print(self.generate_confirmation())

    # String method to display confirmation clearly
    def __str__(self):
        return self.generate_confirmation()