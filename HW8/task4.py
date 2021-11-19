def is_prime(number):
    """Checks if number is prime."""
    if number == 2:
        return True
    elif number == 1:
        return False
    else:
        for i in range(2, int(number/2)):
            if number % i == 0:
                return False
    return True


number = int(input("Please enter number.\n"))

if is_prime(number):
    print(f"Yes, number {number} is prime.")
else:
    print(f"No, number {number} is not prime.")
