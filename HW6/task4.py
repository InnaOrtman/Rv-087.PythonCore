input_tuple = (1, 2, 3, 4, 5, "A", "B", "C", "D", "E", "A1", "A2", "A3", "A4", "A5", "\u0394", "\U0001F600")
numbers_tuple = tuple([x for x in input_tuple if isinstance(x, int)])
letters_tuple = tuple([x for x in input_tuple if str(x).isalpha()])
other_tuple = tuple([x for x in input_tuple if not str(x).isalpha() and not isinstance(x, int)])


print(numbers_tuple)
print(letters_tuple)
print(other_tuple)
