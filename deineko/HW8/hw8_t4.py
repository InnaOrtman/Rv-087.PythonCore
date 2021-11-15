def isPrime(number):
    for i in range(1, number):
        if number%(i + 1) == 0:
            i += 1
            return False
        else:
            return True

number = int(input('Enter a number in range from 1 to 1000: '))
print(isPrime(number))