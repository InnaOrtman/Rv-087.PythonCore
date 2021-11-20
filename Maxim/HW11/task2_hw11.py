# Task 2
# Suppose you are a cook and you have a lot of lettuce so you’ve
# decided to add it to all the dishes.
# Create a few collections that contain the ingredients of dish;
# create function that outputs the ingredients of each dish.
# Create decorator that adds lettuce to all the dishes.


cheesePizza = ["Creamy garlic Parmesan sauce", "Cheese", "Toasted Parmesan"]
pepperoniPizza = ("Marinara sauce", "Cheese", "Pepperoni")
meatPizza = ["Marinara sauce", "Pepperoni", "Italian sausage",
             "Slow-roasted ham", "Hardwood smoked bacon",
             "Seasoned pork and beef"]


def decorMashr(func):
    def inner(*pica):
        func(*pica)
        print("Mushrooms")
    return inner


def decorBasilica(func):
    def inner(*pica):
        func(*pica)
        print("Basilica")
    return inner


def decorOlive(func):
    def inner(*pica):
        func(*pica)
        print("Olive")
    return inner


def decorTakeoutBox(func):
    def inner(*pica):
        func(*pica)
        print("Takeout box")
    return inner


def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
print("." * 35)
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
print("." * 35)
outputIngred(meatPizza)
print("\nCheesePizza")
print("." * 35)
outputIngred(cheesePizza)
print("#" * 40)


@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
print("." * 35)
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
print("." * 35)
outputIngred(meatPizza)


@decorBasilica
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nCheese pizza")
print("." * 35)
outputIngred(cheesePizza)


@decorOlive
@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
print("." * 35)
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
print("." * 35)
outputIngred(meatPizza)


@decorTakeoutBox
@decorOlive
@decorBasilica
@decorMashr
def outputIngred(collection):
    for i in collection:
        print(i)


print("\nPapperoni")
print("." * 35)
outputIngred(pepperoniPizza)
print("\nMeat Pizza")
print("." * 35)
outputIngred(meatPizza)
print("\nCheese pizza")
print("." * 35)
outputIngred(cheesePizza)
