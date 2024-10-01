# Class representing a Customer
class Customer:
    def __init__(self, name, email, phone, customer_id, address):
        # Initializing customer attributes
        self._name = name  # Customer's name
        self._email = email  # Customer's email address
        self._phone = phone  # Customer's phone number
        self._customer_id = customer_id  # Unique identifier for the customer
        self._address = address  # Customer's address

    # Getter methods to access private attributes
    def get_name(self):
        return self._name  # Return customer's name

    def get_email(self):
        return self._email  # Return customer's email

    def get_phone(self):
        return self._phone  # Return customer's phone number

    def get_customer_id(self):
        return self._customer_id  # Return customer ID

    def get_address(self):
        return self._address  # Return customer's address

    # Setter methods to modify private attributes
    def set_name(self, name):
        self._name = name  # Set customer's name

    def set_email(self, email):
        self._email = email  # Set customer's email

    def set_phone(self, phone):
        self._phone = phone  # Set customer's phone number

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id  # Set customer ID

    def set_address(self, address):
        self._address = address  # Set customer's address

    # Placeholder method for searching available rooms
    def search_for_available_rooms(self):
        """ This function should allow the customer to search for available rooms. """
        pass  # Implementation will be added later

    # Placeholder method for booking a room
    def book_room(self, reservation):
        """ This function should allow the customer to book a room. """
        pass  # Implementation will be added later

    # Placeholder method for modifying a reservation
    def modify_reservation(self, reservation_id):
        """ This function should allow the customer to modify an existing reservation. """
        pass  # Implementation will be added later

    # Placeholder method for canceling a reservation
    def cancel_reservation(self, reservation_id):
        """ This function should allow the customer to cancel an existing reservation. """
        pass  # Implementation will be added later


# Class representing a Room Reservation
class Reservation:
    def __init__(self, reservation_id, room, check_in_date, check_out_date, status):
        # Initializing reservation attributes
        self._reservation_id = reservation_id  # Unique reservation ID
        self._room = room  # Room associated with the reservation
        self._check_in_date = check_in_date  # Check-in date for the reservation
        self._check_out_date = check_out_date  # Check-out date for the reservation
        self._status = status  # Reservation status (e.g., Confirmed, Cancelled)

    # Getter methods to access private attributes
    def get_reservation_id(self):
        return self._reservation_id  # Return reservation ID

    def get_room(self):
        return self._room  # Return the room object

    def get_check_in_date(self):
        return self._check_in_date  # Return check-in date

    def get_check_out_date(self):
        return self._check_out_date  # Return check-out date

    def get_status(self):
        return self._status  # Return reservation status

    # Setter methods to modify private attributes
    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id  # Set reservation ID

    def set_room(self, room):
        self._room = room  # Set the room object

    def set_check_in_date(self, check_in_date):
        self._check_in_date = check_in_date  # Set check-in date

    def set_check_out_date(self, check_out_date):
        self._check_out_date = check_out_date  # Set check-out date

    def set_status(self, status):
        self._status = status  # Set reservation status

    # Placeholder method to modify an existing reservation
    def modify_reservation(self, new_details):
        """ This function should modify an existing reservation. """
        pass  # Implementation will be added later

    # Placeholder method to cancel a reservation
    def cancel_reservation(self):
        """ This function should cancel the reservation. """
        pass  # Implementation will be added later


# Class representing a Room in the hotel
class Room:
    def __init__(self, room_number, room_type, price, availability_status, floor):
        # Initializing room attributes
        self._room_number = room_number  # Room number
        self._room_type = room_type  # Room type (e.g., Single, Double)
        self._price = price  # Price per night for the room
        self._availability_status = availability_status  # Room availability status (True for available)
        self._floor = floor  # Floor number where the room is located

    # Getter methods to access private attributes
    def get_room_number(self):
        return self._room_number  # Return room number

    def get_room_type(self):
        return self._room_type  # Return room type

    def get_price(self):
        return self._price  # Return room price

    def get_availability_status(self):
        return self._availability_status  # Return availability status

    def get_floor(self):
        return self._floor  # Return floor number

    # Setter methods to modify private attributes
    def set_room_number(self, room_number):
        self._room_number = room_number  # Set room number

    def set_room_type(self, room_type):
        self._room_type = room_type  # Set room type

    def set_price(self, price):
        self._price = price  # Set room price

    def set_availability_status(self, availability_status):
        self._availability_status = availability_status  # Set availability status

    def set_floor(self, floor):
        self._floor = floor  # Set floor number

    # Placeholder method to check room availability
    def check_availability(self):
        """ This function should check the availability of the room. """
        pass  # Implementation will be added later

    # Placeholder method to get room price information
    def get_price_info(self):
        """ This function should return the price of the room. """
        pass  # Implementation will be added later


# Class representing a Hotel Staff member
class HotelStaff:
    def __init__(self, staff_id, name, position, shift, department):
        # Initializing staff attributes
        self._staff_id = staff_id  # Unique staff ID
        self._name = name  # Staff member's name
        self._position = position  # Staff member's position (e.g., Manager, Receptionist)
        self._shift = shift  # Staff member's shift (e.g., Morning, Night)
        self._department = department  # Department where staff member works

    # Getter methods to access private attributes
    def get_staff_id(self):
        return self._staff_id  # Return staff ID

    def get_name(self):
        return self._name  # Return staff member's name

    def get_position(self):
        return self._position  # Return staff position

    def get_shift(self):
        return self._shift  # Return staff shift

    def get_department(self):
        return self._department  # Return department

    # Setter methods to modify private attributes
    def set_staff_id(self, staff_id):
        self._staff_id = staff_id  # Set staff ID

    def set_name(self, name):
        self._name = name  # Set staff member's name

    def set_position(self, position):
        self._position = position  # Set staff position

    def set_shift(self, shift):
        self._shift = shift  # Set staff shift

    def set_department(self, department):
        self._department = department  # Set department

    # Placeholder method to check in a customer
    def check_in_customer(self, customer):
        """ This function should check in the customer. """
        pass  # Implementation will be added later

    # Placeholder method to check out a customer
    def check_out_customer(self, customer):
        """ This function should check out the customer. """
        pass  # Implementation will be added later


# Creating a Room object for the reservation
room = Room(101, "2 Queen Beds", 89.95, True, 2)

# Creating a Customer object for the booking
customer = Customer("Ted Vera", "tedvera@mac.com", "505-661-1110", 52523687, "2455 Trinity Drive, Los Alamos, NM 87544")

# Creating a Reservation object for the customer
reservation = Reservation(15549850358, room, "2024-08-22", "2024-08-24", "Confirmed")

staff = HotelStaff(101, "John", "Receptionist", "Morning", "Front Desk")

receipt_border = "=" * 50
section_divider = "-" * 50

# Displaying the customer's reservation details similar to Figure 1
print(receipt_border)
print(" " * 10 + "HOTEL RESERVATION RECEIPT")
print(receipt_border)
print(f"Your Reservation Is Confirmed")
print(f"Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
print(section_divider)
print(f"Guest Name: {customer.get_name()}")
print(f"Email: {customer.get_email()}")
print(f"Priceline Trip Number: {reservation.get_reservation_id()}")
print(f"Hotel Confirmation Number: {customer.get_customer_id()}")
print(section_divider)

# Hotel information
print(f"{customer.get_address()}")
print(f"Check-In: Sun, Aug 22, 2024 - 03:00 PM")
print(f"Check-Out: Tue, Aug 24, 2024 - 12:00 PM")
print(f"Number of Nights: 2")
print(f"Number of Rooms: 1")
print(section_divider)

# Room information
print(f"Room 1: {customer.get_name()}")
print(f"Room Type: {room.get_room_type()} / No Smoking / Desk / Safe / Coffee Maker In Room / Hair Dryer")
print(section_divider)

# Summary of Charges
room_cost_per_night = room.get_price()
num_nights = 2
room_subtotal = room_cost_per_night * num_nights
taxes_and_fees = 21.58
total_charges = room_subtotal + taxes_and_fees

print(f"Summary of Charges".center(50))
print(f"Billing Name: {customer.get_name()}")
print(f"Credit Card: Mastercard (ending in 9904)")
print(f"Room Cost: ${room_cost_per_night:.2f} avg. per room, per night")
print(f"Rooms: 1")
print(f"Nights: {num_nights}")
print(f"Room Subtotal: ${room_subtotal:.2f}")
print(f"Taxes and Fees: ${taxes_and_fees:.2f}")
print(f"Total Charges: ${total_charges:.2f}")
print(receipt_border)
print(" " * 15 + "Thank you for choosing our hotel!")
print(receipt_border)
