# task_5

x = input("Enter something:\n")
a = tuple(x)
print(a)

data = a
def find_index(embedded_elem, data_set):
    for elem in data_set:
        if embedded_elem in elem:
            print(data.index(elem))

n = input("Enter the character from the tuple you entered, whose index you want to know: ")
find_index(n, data)

