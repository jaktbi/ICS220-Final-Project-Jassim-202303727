# Import Facility class
from facility import Facility

# Import TimeSlot class
from time_slot import TimeSlot

# Import DataManager class
from data_manager import DataManager


# Create DataManager object
data_manager = DataManager()

# Create facility 1
facility1 = Facility(
    "F001",
    "Study Room A",
    "Study Room",
    6,
    0.0,
    True
)

# Create time slot for facility 1
slot1 = TimeSlot(
    "TS001",
    "2026-05-01",
    "10:00",
    "11:00",
    False,
    0
)

# Add time slot to facility 1
facility1.add_time_slot(slot1)

# Create facility 2
facility2 = Facility(
    "F002",
    "Sports Court A",
    "Sports Court",
    20,
    50.0,
    True
)

# Create time slot for facility 2
slot2 = TimeSlot(
    "TS002",
    "2026-05-01",
    "12:00",
    "13:00",
    False,
    0
)

# Add time slot to facility 2
facility2.add_time_slot(slot2)

# Create facility 3
facility3 = Facility(
    "F003",
    "Event Hall A",
    "Event Hall",
    100,
    200.0,
    True
)

# Create time slot for facility 3
slot3 = TimeSlot(
    "TS003",
    "2026-05-01",
    "15:00",
    "17:00",
    False,
    0
)

# Add time slot to facility 3
facility3.add_time_slot(slot3)

# Save facilities into Pickle file
data_manager.save_facilities([facility1, facility2, facility3])

# Print confirmation message
print("Sample facilities and time slots saved successfully.")