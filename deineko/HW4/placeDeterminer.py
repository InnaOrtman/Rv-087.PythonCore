print('Enter your place number')
place = int(input())

if place < 37 and place % 2 == 0 and place != 0:
    pr = 'is top and compartment'
elif place < 37 and place % 2 != 0:
    pr = 'is bottom and compartment'
elif place >= 37 and place <= 54:
    pr = 'is side'
else:
    pr = 'doesn\'t exist'

print('Place №', place, pr)