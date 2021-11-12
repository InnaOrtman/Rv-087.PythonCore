def calculator(x, y, operation):
    if operation == '+':
        answer = x + y
        return answer
    elif operation == '-':
        answer = x - y
        return answer
    elif operation == '*':
        answer = x*y
        return answer
    elif operation == '/':
        answer = x/y
        return answer
    else:
        answer = 'Unknown operation'
        return answer

print(calculator(5,3,'-'))
    
