p = int(input("Please enter P.\n"))
h = int(input("Please enter H.\n"))

sum_less_p = 0
product_greater_h = 1
number_range_p_h = 0
number = 0

while int(number) != p and int(number) != h:
    number = int(input("Please enter the number.\n"))
    if number < p:
        sum_less_p += number
    if number > h:
        product_greater_h *= number
    if p < number < h or h < number < p:
        number_range_p_h += 1

print(f"Sum of numbers less than P = {sum_less_p}.")
print(f"Product of numbers greater than H = {product_greater_h}")
print(f"Amount of numbers between P and H = {number_range_p_h}")