# task_1

def function(x, y, z):
    if z == "*":
        r = x * y
        return r
    elif z == "/":
        r = x / y
        return r
    elif z == "+":
        r = x + y
        return r
    elif z == "-":
        r = x - y
        return r
    else:
        return "Unknown operation"


print(function(4, 2, "*"))
print(function(4, 2, "/"))
print(function(4, 2, "+"))
print(function(4, 2, "%"))


