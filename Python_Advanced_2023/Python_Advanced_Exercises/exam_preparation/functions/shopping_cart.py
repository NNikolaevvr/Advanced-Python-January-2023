def shopping_cart(*args, **kwargs):




    meals = {'Soup': [], 'Pizza': [], 'Dessert': []}


    for tuple_ in args:
        if tuple_ == 'Stop':
            break
        key = tuple_[0]
        value = tuple_[1]
        if key not in meals:
            meals[key] = []
        if value not in meals[key]:
            if key == 'Pizza' and len(meals[key]) < 4:

                meals[key].append(value)

            elif key == 'Soup' and len (meals['Soup']) < 3:
                meals[key].append(value)

            elif key == 'Dessert' and len(meals['Dessert']) < 2:
                meals[key].append(value)


    sorted_values = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    for value in meals.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    result = ''
    for tuple_ in sorted_values:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))



