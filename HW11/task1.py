def calculator(arg):

    def sum(a, b):
        return a + b

    def dif(a, b):
        return a - b

    def product(a, b):
        return a * b

    def fraction(a, b):
        return a / b

    if arg == 1:
        return sum
    if arg == 2:
        return dif
    if arg == 3:
        return product
    if arg == 4:
        return fraction




a = calculator(1)
b = calculator(2)
c = calculator(3)
d = calculator(4)
print(a(10, 5))
print(b(10, 5))
print(c(10, 5))
print(d(10, 5))