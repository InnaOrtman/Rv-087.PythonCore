# Task 3
# Display a multiplication table (1 to 9).


for i in range(10):
    for j in range(10):
        end = ""
        endMul = "    "
        if len(str(j)) == 1:
            end = "    "

        if i == 0 and j == 0:
            print(" ", end=end)
        elif i == 0 and j != 0:
            if len(str(j)) == 1:
                print(j, end=end)
        elif i != 0 and j == 0:
            print(i, end=end)
        else:
            mul = i * j
            if len(str(mul)) != 1:
                endMul = "   "
            print(mul, end=endMul)
    print()
