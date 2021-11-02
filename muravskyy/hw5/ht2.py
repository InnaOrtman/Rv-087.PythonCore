mylist = []
count = 0 
while len(mylist) < 10:
    number = int(input('enter 10 numbers up 2\t'))

    
    if number <= 2:
        print('your number isn\'t up 2\tenter valid values')
        continue
    mylist += [number]
for i in mylist:
    if i%5 == 0:
        count += 1
print(count)