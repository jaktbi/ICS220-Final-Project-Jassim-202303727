# Import all classes needed to run the system demo
from access_type import AccessType
from user import User
from administrator import Administrator
from facility import Facility
from time_slot import TimeSlot
from booking import Booking
from data_manager import DataManager


# Create Standard Access object
standard_access = AccessType(
    "Standard",
    ["Study Room"],
    1,
    "Can book study rooms only"
)

# Create Premium Access object
premium_access = AccessType(
    "Premium",
    ["Study Room", "Sports Court", "Event Hall"],
    2,
    "Can book all facility types with priority access"
)

# Create normal user object
user1 = User(
    "U001",
    "Jassim",
    "jassim@zu.ac.ae",
    "12345",
    "0500000000",
    standard_access
)

# Create administrator object
admin1 = Administrator(
    "AUSER001",
    "Yas",
    "yas@zu.ac.ae",
    "admin123",
    "0501111111",
    premium_access,
    "A001",
    "Campus Services",
    "System Administrator"
)

# Create facility object
facility1 = Facility(
    "F001",
    "Study Room A",
    "Study Room",
    6,
    0.0,
    True
)

# Create time slot object
slot1 = TimeSlot(
    "TS001",
    "2026-05-01",
    "10:00",
    "11:00",
    False,
    0
)

# Add time slot to facility
facility1.add_time_slot(slot1)

# Create booking object
booking1 = Booking(
    "B001",
    "2026-04-25",
    "Pending",
    0.0,
    user1,
    facility1,
    slot1
)

# Confirm booking
result = booking1.confirm_booking()

# Print booking result
print(result)

# Print booking summary
print("\n--- Booking Summary ---")
print(booking1.generate_booking_summary())

# Print booking confirmation
print("\n--- Booking Confirmation ---")
print(booking1.get_booking_confirmation())

# Create DataManager object
data_manager = DataManager()

# Save data using Pickle
data_manager.save_users([user1, admin1])
data_manager.save_facilities([facility1])
data_manager.save_bookings([booking1])
data_manager.save_confirmations([booking1.get_booking_confirmation()])

# Load data using Pickle
loaded_users = data_manager.load_users()
loaded_facilities = data_manager.load_facilities()
loaded_bookings = data_manager.load_bookings()
loaded_confirmations = data_manager.load_confirmations()

# Print loaded data results
print("\n--- Loaded Data From Pickle Files ---")
print("Users loaded:", len(loaded_users))
print("Facilities loaded:", len(loaded_facilities))
print("Bookings loaded:", len(loaded_bookings))
print("Confirmations loaded:", len(loaded_confirmations))