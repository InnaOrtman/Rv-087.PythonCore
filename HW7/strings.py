initial_dict = {1: "one", 2: "two", 3: "three"}
resulting_dict = {}

for key in initial_dict:
    resulting_dict[initial_dict[key]] = key

print(resulting_dict)