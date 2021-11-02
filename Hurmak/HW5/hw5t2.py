multi5 = 0
for i in range(10):
    num = int(input('enter natural number greater than 2:'))
    if num % 5 == 0:
        multi5 += 1
print(f'{multi5} numbers that are multiples of 5' if multi5 != 1 else f'{multi5} number that is multiple of 5')
