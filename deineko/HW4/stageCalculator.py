print('Enter stage radius value') #5
r =int(input())
print('Enter hall sqare value') #81
s = int(input())
print('Enter k value')  #3
k =int(input())


if s**(1/2) >= (r*2)+(k*2):
   print('It is possible')
else:
   print('It is impossible')

