# Task 1
# User enters two numbers: a and b. Swap the values of variables a and b
#   without using the additional variable.

a = input('Enter value of variable "a": ')
b = input('Enter value of variable "b": ')

print(f'Value of variable "a": {a}, value of variable "b": {b} \n')

a, b = b, a

print('After swap variables "a" and "b":')
print(f'Value of variable "a": {a}, value of variable "b": {b}')
