def calculator(x, y, operation):
    if operation == '+':
        answer = x + y
    elif operation == '-':
        answer = x - y 
    elif operation == '*':
        answer = x*y
    elif operation == '/':
        if y == 0:
            answer = 'y can not be 0'
        else:
            answer = x/y
    else:
        answer = 'Unknown operation'

    return answer

print(calculator(5,5,'+'))
    
