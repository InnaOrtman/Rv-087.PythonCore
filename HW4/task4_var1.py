#A bit more obscure, but fits into task description.

PI = 3.1415
square_area = int(input("Please input square area.\n"))

if (not (square_area ** 0.5).is_integer()) or square_area < 4:
    square_area = int(input("Please input whole number that is over 4\n"))

square_side = square_area ** 0.5

passage_distance = int(input("Please enter passage distance.\n"))

if passage_distance < 0 or passage_distance > square_area ** 0.5:
    passage_distance = int(input("please input passage distance that is over zero and is less than square root of square area.\n"))

max_circle_radius = (square_side - passage_distance) / 2
max_circle_area = PI * max_circle_radius**2

print(f"Max circle radius that can fit into square with passage of {passage_distance} is {max_circle_area}")
circle_area = int(input("please input circle area.\n"))

if circle_area <= 0:
    circle_area = int(input("please input circle area that is over zero.\n"))
    

square_side = square_area ** 0.5
max_circle_radius = (square_side - passage_distance) / 2



if circle_area > max_circle_area:
    print(f"Your circle area is too big, it will not fit")
else:
    print(f"Your circle area is okay, it will fit.")