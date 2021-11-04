tuppy = 1, 'b', '*', -5
print(tuppy)
print('Enter tuple element to find its index or any other to quit:')
while True:
    found = False
    fromTuppy = input()
    for i in tuppy:
        if str(i) == fromTuppy:
            print(f'Index of entered element is {tuppy.index(i)}')
            found = True
    if not found:
        break
