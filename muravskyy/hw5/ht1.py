import random


guess = 0
random_number = random.randint(0, 100)
while guess < 10:
    number = int(input('enter number from 0 to 100\n'))  
    

    if number == random_number: 
        print('\tYou Win !!!')   
        break
    elif number < random_number:
        print('\tyour number is less')
    else:
        print('\tyour number is more')  
    guess += 1
else:       
    print('\tYou lose\tThe number was',random_number) 