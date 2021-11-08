money = int(input('put money'))

if money % 200 == 0:
    a = money//200 
elif money % 100 == 0:
    a=money//100
elif money % 10 == 0:
    a=money//10
else:
    a=money//200,(money%200)//100, ((money%200)%100)//10, (((money%200)%100)%10)//1
print(a)