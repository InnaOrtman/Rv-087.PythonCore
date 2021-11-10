def is_prime(num:int):
    for i in range(2, num):
        if i % num == 0:
            return False
    return True

print(is_prime(33))