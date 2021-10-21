choice = int(input('\nenter your choice, please\n1-rectangle \t2-triangle, \t3-circle\n\n' ))


if choice == 1:
    a = float(input('enter side a of rectangle'))
    b = float(input('enter side b of rectangle'))


    print('square of rectangle is\t',(a * b))

elif choice == 2:
    a = float(input('enter side a of triangle'))
    b = float(input('enter side b of triangle'))
    c = float(input('enter side с of triangle'))


    p = (a+b+c) / 2
    s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    if s == 0:
        print('that is not triangle')
    else:
        print('square of triangle is\t', round(s, 2))
elif choice == 3:
    a = float(input('enter radius of circle')) 
    print('square of circle is\t', (3.14 *(a**2)))
else:
    print('your enter is not 1 2 3')    
