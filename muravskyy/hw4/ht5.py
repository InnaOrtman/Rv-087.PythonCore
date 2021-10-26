money = int(input('enter amount of money\t'))


b200 = 200
b100 = 100
b10 = 10
b1 = 1
if money % b200 == 0:
    b200 = (money // b200)
else:
    b200 = money // b200
    money = money - (b200*200)
    if money % b100 == 0:
        b100 = money // b100
    else:
        b100 = money // b100
        money = money - (b100*100)
        if money % b10 == 0:
            b10 = money // b10
            b1 = 0
        else:
            b10 = money // b10
            money = money - (b10*10)
            b1 = money // b1
print(' 200\t', b200, 'bills\n', '100\t', b100, 'bills\n', '10\t', b10, 'bills\n','1\t', b1,'bills')            
