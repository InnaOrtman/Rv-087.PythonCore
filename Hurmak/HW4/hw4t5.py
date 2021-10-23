amount = int(input("enter amount:"))
banknotes = {200: 0, 100: 0, 10: 0, 1: 0}
print('Your amount exchanged with:')
for i in banknotes.keys():
    if amount >= i:
        banknotes[i] = amount // i
        amount = amount - banknotes[i]*i
        print(f' {i} - {banknotes[i]}')
