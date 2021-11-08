first_string = "Hello, my name is Kirill, i study Python at Softserve. 111 + 222 = 333"
second_string = "Howdy, anything new in year 2021, fellow past-dwellers? By time-traveler."


mod_set_first = set([x for x in first_string if str(x).isalpha()])
mod_set_second = set([x for x in second_string if str(x).isalpha()])

print(f"Set one: {mod_set_first}")
print(f"Set two: {mod_set_second}")

print(f"All the letters of both sets: {sorted(mod_set_first.union(mod_set_second))}")