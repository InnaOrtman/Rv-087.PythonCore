num = 1
neg = 0
pos = 0
while num != 0:
    num = int(input('Enter a number:'))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print(pos, neg)
print(f'{pos*100/(pos+neg)}% of positive and {100-pos*100/(pos+neg)}% of negative')
