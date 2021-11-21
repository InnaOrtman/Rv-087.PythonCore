def sum(a, b):
    return a + b

def dif(a, b):
    return a - b

def product(a, b):
    return a * b

def fraction(a, b):
    try:
        return a / b 
    except ZeroDivisionError :
        return 'divisor cannot be Zero'