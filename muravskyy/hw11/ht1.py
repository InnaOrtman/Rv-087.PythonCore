def calculator(arg):
    def sum(a, b):
        return a + b
    def dif(a, b):
        return a -b
    def product(a, b):
        return a * b
    def fraction(a, b):
        try:
            return a / b 
        except ZeroDivisionError :
            return 'divisor cannot be Zero'
    if arg == 1:
        return sum
    elif arg == 2:
        return dif
    elif arg == 3:
        return product
    elif arg == 4:
        return fraction

print(calculator(2)(3, 2))