def shop_from_grocery_list(budget, grocery_list, *products_info):
    for product, price in products_info:
        if product in grocery_list:
            if price <= budget:
                budget -= price
                grocery_list.remove(product)
            else:
                break

    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f'You did not buy all the products. Missing products: {", ".join(x for x in grocery_list)}.'


# Test code 1
print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

# Test code 2
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

# Test code 3
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
