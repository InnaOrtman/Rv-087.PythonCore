CARRIAGE_SEATS_MAX = 54

seat_number = int(input(f"Please enter value from 1 to {CARRIAGE_SEATS_MAX}.\n"))

if seat_number % 2 == 0:
    seat_level = "top"
else:
    seat_level = "bottom"
if seat_number >= 37:
    is_side_seat = "side"
else:
    is_side_seat = "not side"

print(f"Seat number {seat_number} is {seat_level} and {is_side_seat}")