#A bit easier and way more user-friendly as users don't usually know how circle and square areas behave themself.

PI = 3.1415
square_side = int(input("Please input square side.\n"))

circle_radius = float(input("please input circle radius.\n"))

passage_distance = int(input("Please enter passage distance.\n"))


if circle_radius <= (square_side - passage_distance) / 2:
    print(f"your circle area will be {PI * circle_radius**2} which will fit square with area of {square_side**2}")
else:
    print(f"your circle area will be {PI * circle_radius**2} which will not fit square with area of {square_side**2}")
