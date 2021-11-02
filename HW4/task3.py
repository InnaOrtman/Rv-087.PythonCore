number = int(input("Please enter a number\n"))
digits = len(str(number))
if number < 0:
    digits -= 1

if number < 0:
    print(f"{number} is negative {digits}-digit number")
elif number > 0:
    print(f"{number} is positive {digits}-digit number")
else:
    print(f"The number is zero, single-digit number that is neither positive nor negative")

