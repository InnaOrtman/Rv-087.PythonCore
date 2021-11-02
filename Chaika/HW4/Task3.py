# Task 3
# The user enters a number, the program must display its description. For example, "positive one-digit", "negative two-digit", etc.
# Задача 3
# Пользователь вводит число, программа должна отображать его описание. Например, «положительное однозначное число», «отрицательное двузначное число» и т. Д.

num = int(input('input number: '))
leng = len(str(num))

if leng == 1 and num > 0:
    print("number ", num, " positive one-digit")

elif leng == 2 and num > 0:
    print("number ", num, " positive two-digit")

elif leng == 2 and num < 0:
    print("number ", num, " negative one-digit")

elif leng == 3 and num < 0:
    print("number ", num, " negative two-digit") 

else:
    print("the number is not in the search scope")