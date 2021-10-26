# task_1

year = int(input("Which year do you want to check? "))

# тут пепевіряємо чи високосний
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap")
    else:
     print("Not leap")
  else:
     print("Leap")
else:
  print("Not leap")

# тут пепевіряємо століття

if (year <= 100):
    print("1st century")
elif year % 100 == 0:
    print(year // 100,"century")
else:
    print(year // 100 + 1,"century")
