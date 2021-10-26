import math


monye = int(input('enter amount of money\t'))


bank = (200,100,10,1)
for x in bank:
    quantity = math.floor(monye/x)
    monye = monye - (quantity*x)
    a = {x:quantity}     
    print("{value[0]} \t {value[1]} bills".format(value = [x, a[x]]))
       