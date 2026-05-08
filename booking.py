# Import BookingConfirmation class
from booking_confirmation import BookingConfirmation


# Booking class represents a facility reservation
class Booking:

    # Constructor to initialize booking object
    def __init__(self, booking_id, booking_date,
                 status, total_cost,
                 user, facility, time_slot):

        # Store booking attributes as private
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__status = status
        self.__total_cost = total_cost

        # Store related objects as private
        self.__user = user
        self.__facility = facility
        self.__time_slot = time_slot

        # Store booking confirmation object
        self.__booking_confirmation = None

    # Getter method to return booking ID
    def get_booking_id(self):
        return self.__booking_id

    # Getter method to return booking date
    def get_booking_date(self):
        return self.__booking_date

    # Getter method to return booking status
    def get_status(self):
        return self.__status

    # Getter method to return total cost
    def get_total_cost(self):
        return self.__total_cost

    # Getter method to return user object
    def get_user(self):
        return self.__user

    # Getter method to return facility object
    def get_facility(self):
        return self.__facility

    # Getter method to return time slot object
    def get_time_slot(self):
        return self.__time_slot

    # Setter method to update booking status
    def set_status(self, status):
        self.__status = status

    # Setter method to update total cost
    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    # Method to calculate booking cost
    def calculate_booking_cost(self):

        # Get booking fee from facility object
        self.__total_cost = self.__facility.get_booking_fee()

        # Return calculated booking cost
        return self.__total_cost

    # Method to validate booking
    def validate_booking(self):

        # Check if selected time slot is available
        if self.__time_slot.check_slot_availability():

            # Check if user access type allows this facility type
            access = self.__user.get_access_type()

            if access.can_book_facility_type(
                    self.__facility.get_facility_type()):

                return True

        # Return False if validation fails
        return False

    # Method to confirm booking
    def confirm_booking(self):

        # Validate booking before confirmation
        if self.validate_booking():

            # Reserve selected time slot
            self.__time_slot.reserve_slot()

            # Calculate booking cost
            self.calculate_booking_cost()

            # Update booking status
            self.__status = "Confirmed"

            # Create confirmation object
            self.__booking_confirmation = BookingConfirmation(
                "CONF-" + self.__booking_id,
                self.__booking_date,
                f"{self.__facility.get_facility_name()} | "
                f"{self.__time_slot.display_slot_details()}",
                self.__total_cost
            )

            # Add booking to user booking history
            self.__user.add_booking_to_history(self)

            # Return success message
            return "Booking confirmed successfully."

        # Return failure message if validation fails
        return "Booking validation failed."

    # Method to modify booking
    def modify_booking(self):
        # This method should modify existing booking details
        pass

    # Method to delete booking
    def delete_booking(self):

        # Release reserved slot
        self.__time_slot.release_slot()

        # Update booking status
        self.__status = "Deleted"

    # Method to generate booking summary
    def generate_booking_summary(self):

        # Return formatted booking summary
        return (f"Booking ID: {self.__booking_id}\n"
                f"User: {self.__user.get_name()}\n"
                f"Facility: {self.__facility.get_facility_name()}\n"
                f"Status: {self.__status}\n"
                f"Total Cost: AED {self.__total_cost}")

    # Getter method to return confirmation object
    def get_booking_confirmation(self):
        return self.__booking_confirmation

    # String method to display booking clearly
    def __str__(self):
        return self.generate_booking_summary()