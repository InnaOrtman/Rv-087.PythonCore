lst = []
multiplesFive = []
for i in range(10):
    numbers = int(input('Enter a number greater than 2 '))
    if (numbers % 5 == 0):
        lst.append(numbers)
        multiplesFive.append(numbers) 
    else:
        lst.append(numbers)

print('Your list of numbers is ', lst, 'but only ', multiplesFive, 'are multiples of 5')

