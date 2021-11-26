# Task 2
# Suppose you are a cook and you have a lot of lettuce so you’ve
# decided to add it to all the dishes.
# Create a few collections that contain the ingredients of dish;
# create function that outputs the ingredients of each dish.
# Create decorator that adds lettuce to all the dishes.

from functools import wraps


cheesePizza = ["Creamy garlic Parmesan sauce", "Cheese", "Toasted Parmesan"]
pepperoniPizza = ("Marinara sauce", "Cheese", "Pepperoni")
meatPizza = ["Marinara sauce", "Pepperoni", "Italian sausage",
             "Slow-roasted ham", "Hardwood smoked bacon",
             "Seasoned pork and beef"]


def decorMashr(func):
    @wraps(func)
    def inner(*pica):
        func(*pica)
        print("Mushrooms")
    return inner


def decorBasilica(func):
    @wraps(func)
    def inner(*pica):
        func(*pica)
        print("Basilica")
    return inner


def decorOlive(func):
    @wraps(func)
    def inner(*pica):
        func(*pica)
        print("Olive")
    return inner


def decorTakeoutBox(func):
    @wraps(func)
    def inner(*pica):
        func(*pica)
        print("Takeout box")
    return inner


def decPrint(func):
    @wraps(func)
    def inner(*pica):
        print("." * 35)
        func(*pica)
    return inner


@decPrint
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
outputIngred(meatPizza)
print("\nCheesePizza")
outputIngred(cheesePizza)
print("#" * 40)


@decPrint
@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
outputIngred(meatPizza)


@decPrint
@decorBasilica
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nCheese pizza")
outputIngred(cheesePizza)


@decPrint
@decorOlive
@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
outputIngred(meatPizza)


@decPrint
@decorTakeoutBox
@decorOlive
@decorBasilica
@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
outputIngred(meatPizza)
print("\nCheese pizza")
outputIngred(cheesePizza)
