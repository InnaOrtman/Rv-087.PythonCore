entry_tuple = ("A", "B", "C", "D", "E", 1, 2, 3, 4, 5, "\u0394", "\U0001F600")

print(entry_tuple)

user_input = input("Please enter the symbol \n")

if user_input.isnumeric():
    print(entry_tuple.index(int(user_input)))
else:
    print(entry_tuple.index(user_input))