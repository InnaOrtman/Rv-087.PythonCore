SIZE = 5

outline_symbol = input("Please input outline symbol.\n")
fill_symbol = input("Please input fill symbol.\n")

square = str()

for i in range (1, SIZE+1):
    for j in range(1, SIZE+1):
        if i == 1 or i == SIZE or j == 1 or j == SIZE:
            square += outline_symbol
        else:
            square += fill_symbol
    square += "\n"
print(square)