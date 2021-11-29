burger = ['beef', 'egg', 'onion', \
        'garlic']
sandwiches = ['brown sugar', 'ginger' \
        'boneless chicken thighs', \
        'pepper']
def decorator(func):
    def wrapper(arg):
        print(*func(arg),'salat')
    return wrapper

@decorator
def dish(dish_list):
    return dish_list

dish(burger)
dish(sandwiches)