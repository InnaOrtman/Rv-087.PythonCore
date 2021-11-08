a = int(input('vvedy year a '))
centry=( a // 100) + 1
print (centry)

if a % 100 != 0 and a % 400 == 0:
    print (a , 'vysokosny')
elif a % 4 == 0:
    print (a ,'vysokosny')
