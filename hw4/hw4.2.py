
print ('if choise is rectangle than push - 1')
print ('if choise is triangle than push - 2')
print ('if choise is circl push - 3')

choise = int(input())

if choise  == 1:
    a = int(input('put the first side of  rectangle'))
    b = int (input('put the second side of rectangle'))
    s = a*b
    print (s)
elif choise  == 2:
    a=float(input('push the first side of triangle'))
    b=float(input('push the second side of triangle'))
    c=float(input('push the third side of triangle'))

    p = (a+b+c) / 2
    s = (p * ( p-a ) * ( p-b ) * ( p-c )) ** 0.5
    print (s)
elif choise ==3:
    r=float(input('push radius of circle'))

    s = 3.14 * (r**2)
    print (s)