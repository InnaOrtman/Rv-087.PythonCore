input_numbers = input("Please enter 10 numbers separated by \' \'\n")

list_numbers = input_numbers.split()
dividible_by_5 = 0

for i in list_numbers:
    if int(i) % 5 == 0:
        dividible_by_5 += 1;
        
print(f"There are {dividible_by_5} numbers that are multiple of 5.")