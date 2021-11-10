# task_2

x = int(input("Enter the amount of money ($) you want to deposit, please:\n"))
y = int(input("Enter the term of the deposit (years):\n"))

def deposit(x, y):
    s = x
    for i in range(1, y+1):
        p = (s * 10/100)
        s = s + p
        x += s
    return (round(s, 2))

print(f"After the expiration of the deposit you will receive {deposit(x, y)}$")



