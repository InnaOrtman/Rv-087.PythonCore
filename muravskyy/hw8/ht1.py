def arithmetic(num1, num2,operation:str):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/' and num2 != 0:
        return num1 / num2    
    return 'Unknown operation'

print(arithmetic(1, 0, '/'))
print(arithmetic(2.33, 2.5, '+'))