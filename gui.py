from booking import Booking

# Import tkinter library for creating GUI windows
import tkinter as tk

# Import messagebox to show popup messages
from tkinter import messagebox

# Import AccessType class
from access_type import AccessType

# Import User class
from user import User

# Import DataManager class
from data_manager import DataManager


# Main application class for the GUI
class SmartCampusGUI:

    # Constructor to set up the main window
    def __init__(self):

        # Create the main tkinter window
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Smart Campus Facility Booking System")

        # Set the window size
        self.window.geometry("600x400")

        # Create DataManager object for saving and loading data
        self.data_manager = DataManager()

        # Create main title label
        self.title_label = tk.Label(
            self.window,
            text="Smart Campus Facility Booking System",
            font=("Arial", 18, "bold")
        )

        # Place title label on the window
        self.title_label.pack(pady=30)

        # Create button for account creation
        self.create_account_button = tk.Button(
            self.window,
            text="Create Account",
            width=25,
            command=self.open_create_account
        )

        # Display create account button
        self.create_account_button.pack(pady=10)

        # Create button for user login
        self.login_button = tk.Button(
            self.window,
            text="Log In",
            width=25,
            command=self.open_login
        )

        # Display login button
        self.login_button.pack(pady=10)
        # Create button for making a booking
        self.make_booking_button = tk.Button(
            self.window,
            text="Make Booking",
            width=25,
            command=self.open_make_booking
        )

        # Display make booking button
        self.make_booking_button.pack(pady=10)
        # Create button for deleting/cancelling a booking
        self.delete_booking_button = tk.Button(
            self.window,
            text="Delete Booking",
            width=25,
            command=self.open_delete_booking
        )

        # Display delete booking button
        self.delete_booking_button.pack(pady=10)

       



        # Display make booking button
        self.make_booking_button.pack(pady=10)

        # Create button for admin dashboard
        self.admin_button = tk.Button(
            self.window,
            text="Admin Dashboard",
            width=25,
            command=self.open_admin_dashboard
        )

        # Display admin button
        self.admin_button.pack(pady=10)

        # Create button to exit the system
        self.exit_button = tk.Button(
            self.window,
            text="Exit",
            width=25,
            command=self.window.destroy
        )

        # Display exit button
        self.exit_button.pack(pady=10)

    # Method to open create account window
    def open_create_account(self):

        # Create a new window for account creation
        create_window = tk.Toplevel(self.window)

        # Set create account window title
        create_window.title("Create Account")

        # Set create account window size
        create_window.geometry("400x400")

        # Create title label for create account window
        title = tk.Label(
            create_window,
            text="Create New Account",
            font=("Arial", 16, "bold")
        )

        # Display title label
        title.pack(pady=10)

        # Create label and entry for user ID
        tk.Label(create_window, text="User ID").pack()
        user_id_entry = tk.Entry(create_window, width=30)
        user_id_entry.pack(pady=5)

        # Create label and entry for name
        tk.Label(create_window, text="Name").pack()
        name_entry = tk.Entry(create_window, width=30)
        name_entry.pack(pady=5)

        # Create label and entry for email
        tk.Label(create_window, text="Email").pack()
        email_entry = tk.Entry(create_window, width=30)
        email_entry.pack(pady=5)

        # Create label and entry for password
        tk.Label(create_window, text="Password").pack()
        password_entry = tk.Entry(create_window, width=30, show="*")
        password_entry.pack(pady=5)

        # Create label and entry for phone number
        tk.Label(create_window, text="Phone Number").pack()
        phone_entry = tk.Entry(create_window, width=30)
        phone_entry.pack(pady=5)

        # Inner method to save the created user
        def save_account():

            # Get user input from entry fields
            user_id = user_id_entry.get()
            name = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            phone = phone_entry.get()

            # Check if any field is empty
            if user_id == "" or name == "" or email == "" or password == "" or phone == "":
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            # Create default Standard Access object
            standard_access = AccessType(
                "Standard",
                ["Study Room"],
                1,
                "Can book study rooms only"
            )

            # Create new user object
            new_user = User(
                user_id,
                name,
                email,
                password,
                phone,
                standard_access
            )

            # Load existing users from Pickle file
            users = self.data_manager.load_users()

            # Add new user to users list
            users.append(new_user)

            # Save updated users list using Pickle
            self.data_manager.save_users(users)

            # Show success message
            messagebox.showinfo("Success", "Account created successfully.")

            # Close create account window
            create_window.destroy()

        # Create save button
        save_button = tk.Button(
            create_window,
            text="Save Account",
            width=20,
            command=save_account
        )

        # Display save button
        save_button.pack(pady=15)

    # Method to open login window
    def open_login(self):

            # Create a new window for login
            login_window = tk.Toplevel(self.window)

            # Set login window title
            login_window.title("Log In")

            # Set login window size
            login_window.geometry("350x300")

            # Create title label
            title = tk.Label(
                login_window,
                text="User Login",
                font=("Arial", 16, "bold")
            )

            # Display title label
            title.pack(pady=10)

            # Create label and entry for email
            tk.Label(login_window, text="Email").pack()
            email_entry = tk.Entry(login_window, width=30)
            email_entry.pack(pady=5)

            # Create label and entry for password
            tk.Label(login_window, text="Password").pack()
            password_entry = tk.Entry(login_window, width=30, show="*")
            password_entry.pack(pady=5)

            # Inner method to check login
            def check_login():

                # Get email from entry field
                email = email_entry.get()

                # Get password from entry field
                password = password_entry.get()

                # Load users from Pickle file
                users = self.data_manager.load_users()

                # Loop through users to find matching login details
                for user in users:

                    # Check if email and password match
                    if user.get_email() == email and user.get_password() == password:
                        # Show success message
                        messagebox.showinfo("Success", "Login successful.")

                        # Close login window
                        login_window.destroy()

                        # Stop method after successful login
                        return

                # Show error message if no matching user is found
                messagebox.showerror("Error", "Invalid email or password.")

            # Create login button
            login_button = tk.Button(
                login_window,
                text="Log In",
                width=20,
                command=check_login
            )

            # Display login button
            login_button.pack(pady=15)



    # Method to open make booking window
    def open_make_booking(self):

        # Create a new window for making bookings
        booking_window = tk.Toplevel(self.window)

        # Set booking window title
        booking_window.title("Make Booking")

        # Set booking window size
        booking_window.geometry("500x500")

        # Create title label
        title = tk.Label(
            booking_window,
            text="Make Facility Booking",
            font=("Arial", 16, "bold")
        )

        # Display title label
        title.pack(pady=10)

        # Load users from Pickle file
        users = self.data_manager.load_users()

        # Load facilities from Pickle file
        facilities = self.data_manager.load_facilities()

        # Check if there are users and facilities available
        if len(users) == 0 or len(facilities) == 0:
            messagebox.showerror("Error", "Users or facilities are missing.")
            booking_window.destroy()
            return

        # Create label for user selection
        tk.Label(booking_window, text="Select User").pack()

        # Create user dropdown variable
        user_var = tk.StringVar(booking_window)

        # Create list of user names for dropdown
        user_options = [user.get_name() for user in users]

        # Set default selected user
        user_var.set(user_options[0])

        # Create user dropdown menu
        user_menu = tk.OptionMenu(booking_window, user_var, *user_options)

        # Display user dropdown
        user_menu.pack(pady=5)

        # Create label for facility selection
        tk.Label(booking_window, text="Select Facility").pack()

        # Create facility dropdown variable
        facility_var = tk.StringVar(booking_window)

        # Create list of facility names for dropdown
        facility_options = [facility.get_facility_name() for facility in facilities]

        # Set default selected facility
        facility_var.set(facility_options[0])

        # Create facility dropdown menu
        facility_menu = tk.OptionMenu(booking_window, facility_var, *facility_options)

        # Display facility dropdown
        facility_menu.pack(pady=5)

        # Create booking date label and entry
        tk.Label(booking_window, text="Booking Date").pack()
        booking_date_entry = tk.Entry(booking_window, width=30)
        booking_date_entry.insert(0, "2026-05-01")
        booking_date_entry.pack(pady=5)

        # Inner method to confirm booking
        def confirm_booking_gui():

            # Get selected user name
            selected_user_name = user_var.get()

            # Get selected facility name
            selected_facility_name = facility_var.get()

            # Find selected user object
            selected_user = None
            for user in users:
                if user.get_name() == selected_user_name:
                    selected_user = user

            # Find selected facility object
            selected_facility = None
            for facility in facilities:
                if facility.get_facility_name() == selected_facility_name:
                    selected_facility = facility

            # Validate selected objects
            if selected_user is None or selected_facility is None:
                messagebox.showerror("Error", "Invalid user or facility selection.")
                return

            # Check if the facility has at least one time slot
            if len(selected_facility.get_time_slots()) == 0:
                messagebox.showerror("Error", "No time slots available for this facility.")
                return

            # Select the first available time slot for simplicity
            selected_slot = selected_facility.get_time_slots()[0]

            # Create booking ID based on number of existing bookings
            bookings = self.data_manager.load_bookings()
            booking_id = "B" + str(len(bookings) + 1).zfill(3)

            # Create new booking object
            new_booking = Booking(
                booking_id,
                booking_date_entry.get(),
                "Pending",
                0.0,
                selected_user,
                selected_facility,
                selected_slot
            )

            # Confirm booking using Booking class logic
            result = new_booking.confirm_booking()

            # If booking is confirmed successfully
            if result == "Booking confirmed successfully.":

                # Add booking to list
                bookings.append(new_booking)

                # Save updated bookings list
                self.data_manager.save_bookings(bookings)

                # Load confirmations list
                confirmations = self.data_manager.load_confirmations()

                # Add booking confirmation to confirmations list
                confirmations.append(new_booking.get_booking_confirmation())

                # Save updated confirmations list
                self.data_manager.save_confirmations(confirmations)

                # Show booking confirmation message
                messagebox.showinfo(
                    "Booking Confirmed",
                    new_booking.get_booking_confirmation().generate_confirmation()
                )

                # Close booking window
                booking_window.destroy()

            # If booking validation failed
            else:
                messagebox.showerror("Booking Failed", result)

        # Create confirm booking button
        confirm_button = tk.Button(
            booking_window,
            text="Confirm Booking",
            width=20,
            command=confirm_booking_gui
        )

        # Display confirm booking button
        confirm_button.pack(pady=20)

        # Method to open delete booking window
    def open_delete_booking(self):

            # Create delete booking window
            delete_window = tk.Toplevel(self.window)

            # Set window title
            delete_window.title("Delete Booking")

            # Set window size
            delete_window.geometry("450x350")

            # Create title label
            title = tk.Label(
                delete_window,
                text="Delete Booking",
                font=("Arial", 16, "bold")
            )

            # Display title label
            title.pack(pady=10)

            # Load bookings from Pickle file
            bookings = self.data_manager.load_bookings()

            # Check if bookings exist
            if len(bookings) == 0:
                # Show error message
                messagebox.showerror("Error", "No bookings available.")

                # Close window
                delete_window.destroy()

                return

            # Create label for booking selection
            tk.Label(delete_window, text="Select Booking").pack()

            # Create dropdown variable
            booking_var = tk.StringVar(delete_window)

            # Create booking options list
            booking_options = []

            # Loop through bookings
            for booking in bookings:
                # Create readable booking string
                booking_text = (
                    f"{booking.get_booking_id()} | "
                    f"{booking.get_user().get_name()} | "
                    f"{booking.get_facility().get_facility_name()}"
                )

                # Add booking text to list
                booking_options.append(booking_text)

            # Set default booking option
            booking_var.set(booking_options[0])

            # Create dropdown menu
            booking_menu = tk.OptionMenu(
                delete_window,
                booking_var,
                *booking_options
            )

            # Display dropdown menu
            booking_menu.pack(pady=10)

            # Inner method to delete booking
            def delete_selected_booking():

                # Get selected booking text
                selected_booking = booking_var.get()

                # Create new bookings list
                updated_bookings = []

                # Loop through existing bookings
                for booking in bookings:

                    # Create booking text again
                    booking_text = (
                        f"{booking.get_booking_id()} | "
                        f"{booking.get_user().get_name()} | "
                        f"{booking.get_facility().get_facility_name()}"
                    )

                    # Keep bookings that are NOT selected
                    if booking_text != selected_booking:
                        updated_bookings.append(booking)

                # Save updated bookings list
                self.data_manager.save_bookings(updated_bookings)

                # Show success message
                messagebox.showinfo(
                    "Success",
                    "Booking deleted successfully."
                )

                # Close delete booking window
                delete_window.destroy()

            # Create delete button
            delete_button = tk.Button(
                delete_window,
                text="Delete Booking",
                width=20,
                command=delete_selected_booking
            )

            # Display delete button
            delete_button.pack(pady=20)

    # Method to open admin dashboard
    def open_admin_dashboard(self):

        # Create a new admin dashboard window
        admin_window = tk.Toplevel(self.window)

        # Set admin dashboard title
        admin_window.title("Admin Dashboard")

        # Set admin dashboard size
        admin_window.geometry("600x500")

        # Create dashboard title label
        title = tk.Label(
            admin_window,
            text="Administrator Dashboard",
            font=("Arial", 18, "bold")
        )

        # Display title label
        title.pack(pady=15)

        # Create text area to display system information
        dashboard_text = tk.Text(
            admin_window,
            width=70,
            height=20
        )

        # Display text area
        dashboard_text.pack(pady=10)

        # Load users from Pickle file
        users = self.data_manager.load_users()

        # Load facilities from Pickle file
        facilities = self.data_manager.load_facilities()

        # Load bookings from Pickle file
        bookings = self.data_manager.load_bookings()

        # Display users section
        dashboard_text.insert(tk.END, "========== USERS ==========\n")

        # Loop through all users
        for user in users:
            dashboard_text.insert(
                tk.END,
                f"User ID: {user.get_user_id()} | "
                f"Name: {user.get_name()} | "
                f"Email: {user.get_email()}\n"
            )

        # Add spacing
        dashboard_text.insert(tk.END, "\n")

        # Display facilities section
        dashboard_text.insert(tk.END, "========== FACILITIES ==========\n")

        # Loop through all facilities
        for facility in facilities:
            dashboard_text.insert(
                tk.END,
                f"Facility: {facility.get_facility_name()} | "
                f"Type: {facility.get_facility_type()} | "
                f"Capacity: {facility.get_capacity()}\n"
            )

        # Add spacing
        dashboard_text.insert(tk.END, "\n")

        # Display bookings section
        dashboard_text.insert(tk.END, "========== BOOKINGS ==========\n")

        # Loop through all bookings
        for booking in bookings:
            dashboard_text.insert(
                tk.END,
                f"Booking ID: {booking.get_booking_id()} | "
                f"User: {booking.get_user().get_name()} | "
                f"Facility: {booking.get_facility().get_facility_name()} | "
                f"Status: {booking.get_status()}\n"
            )

        # Disable text editing
        dashboard_text.config(state=tk.DISABLED)

    # Method to run the GUI application
    def run(self):

        # Start the tkinter event loop
        self.window.mainloop()


# Create GUI object only if this file is executed directly
if __name__ == "__main__":

    # Create GUI application object
    app = SmartCampusGUI()

    # Run the application
    app.run()