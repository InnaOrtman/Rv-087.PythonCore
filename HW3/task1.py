a = int(input("Please enter value for a\n"))
b = int(input("Please enter value for b\n"))

print(f"Your entered value for a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b

print(f"Now, a = {a}, b = {b}")