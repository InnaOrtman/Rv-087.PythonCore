# task_3

# Multiplication table (from 1 to 9 or more:))

num = int(input("Enter the number you want to multiply from 1 to 9:\n"))

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
