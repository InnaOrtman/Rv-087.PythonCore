import random 


n = random.randint(1,100)
#print(n)

for i in range (10):
    win = False
    userNumber = int(input('How do you think, which number from 1 to 100 it is? \n'))

    if (userNumber != n and userNumber > n):
        print('No, the number is less')
    elif (userNumber != n and userNumber < n):
        print('No, the number is greater')
    elif (userNumber == n):
        print('Congratulations, you have guessed the number! It is ', n)
        win = True
        break

if (win == False):
    print('You have not guessed the number, it is ',n )
    
    