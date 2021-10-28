total = 0
positive = 0
while True:
    number = int(input('enter the number\n'))
            

    if number == 0:
        break 
    elif number > 0:
        positive += 1
    total += 1    
    print(f'positive - {positive / total * 100:.2f}%\tnegative - {(total-positive) / total * 100:.2f}%')