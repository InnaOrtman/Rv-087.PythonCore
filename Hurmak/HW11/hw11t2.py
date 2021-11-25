def add_let(ingredients):
    def wrapper(*args, **kwargs):
        print('letuce')
        ingredients(*args, **kwargs)
    return wrapper


@add_let
def show_ingredients(dish):
    for i in dish:
        print (i)


caprese=('tomato', 'mozarela', 'basilic')
show_ingredients(caprese)
print('==' * 20)
greek_salad=('Tomatoes', 'cucumber', 'onion', 'feta cheese', 'olives', 'salt')
show_ingredients(greek_salad)
