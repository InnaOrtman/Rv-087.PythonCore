from functools import wraps


def lettufy(func):
    @wraps(func)
    def inner(*args):
        result = list(*args)
        result.append("lettuce")
        return func(tuple(result))
    return inner


@lettufy
def show_dish(*args):
    for i in args:
        print(i)


shawarma = ("meat", "cucumber", "carrot")
soup = ("potato", "pork", "carrot", "water", "spices")
#
# show_dish(shawarma)
# show_dish(soup)



input("type in")