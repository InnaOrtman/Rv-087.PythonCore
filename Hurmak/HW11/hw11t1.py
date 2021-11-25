def calculator(arg):
    if arg == 1: return lambda a, b: a + b
    if arg == 2: return lambda a, b: a - b
    if arg == 3: return lambda a, b: a * b
    if arg == 4: return lambda a, b: a / b

print(calculator(1)(100, 5))
print(calculator(2)(100, 5))
print(calculator(3)(100, 5))
print(calculator(4)(100, 5))
