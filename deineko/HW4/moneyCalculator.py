print('Enter an amount of money')
money = int(input()) 

if money % 200 == 0:
    getMoney =  money//200, '200 UAH banknotes' 
elif money % 100 == 0:
    getMoney = money//100, '100 UAH banknotes' 
elif money % 10 == 0:
    getMoney = money//10, '10 UAH banknotes' 
else:
    getMoney = money//200, '200 UAH banknotes', (money%200)//100, '100 UAH banknotes', ((money%200)%100)//10, '10 UAH banknotes', (((money%200)%100))%10, '1 UAH banknotes'

print('You will get', getMoney) 