# task_4


def is_prime(x):
    y = 2
    while x % y != 0:
        y += 1
    return y == x

print(is_prime(3))
