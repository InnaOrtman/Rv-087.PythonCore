a = int(input("enter the year\n"))


century = a // 100
if a%4 != 0 or (a%100 == 0 and a%400 != 0):
    print(str(century)+'th Century', '\tcommon year')   
else:
    print(str(century)+'th Century', '\tintercalary year')    
