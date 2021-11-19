def calculator(*args):
    """performs magical operations on numbers."""
    math_operators = ('+', '-', '*', '/', '%')
    if args[2] != 0:
        if args[1] in math_operators:
            return eval(f'{args[0]} {args[1]} {args[2]}')
        else:
            return "Unknown operation."


number1 = input("Please enter first number.\n")
number2 = input("Please enter second number.\n")
operator = input("Please enter + or - or * or /.\n")
print(f"{number1} {operator} {number2} = {calculator(number1, operator, number2)}")