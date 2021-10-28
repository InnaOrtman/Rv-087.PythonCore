n = int(input())


a = '#'
b = '+'
for x in range(1, n):
    if x == 1 or x == (n-1):
        print(a * (n-1))
    else:
        print(a+b*(n-3)+a)    