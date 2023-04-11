def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_products = set()
    budget_left = budget

    for product, price in args:
        if product not in grocery_list:
            continue

        if budget_left < price:
            break

        if product in purchased_products:
            continue

        purchased_products.add(product)
        budget_left -= price

    if len(purchased_products) == len(grocery_list):
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        missing_products = set(grocery_list) - purchased_products
        return f"You did not buy all the products. Missing products: {', '.join(sorted(missing_products))}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))