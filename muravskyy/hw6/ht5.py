myTuple = 1 , 2, 3, 'a', 'v', '+','-'
print(myTuple)
count = 0
while count < 7:
    symbol = input('enter symbol\n')
    if str(symbol).isnumeric():
        symbol = int(symbol)
    if symbol in myTuple:
        count += 1
        print('index = ', myTuple.index(symbol))
    print('enter another one')    
    continue