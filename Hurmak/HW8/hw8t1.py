def calculate(x, y, operator):
    if operator == "+": return x + y
    if operator == "-": return x - y
    if operator == "*": return x * y
    if operator == "/": return x / y
    return 'Unknown operation'


print(calculate(1, 4, "@"))
