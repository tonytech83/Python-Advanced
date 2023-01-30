def shopping_cart(*args):
    meal_limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }

    shopping_dict = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set(),
    }
    for line in args:
        if line == 'Stop':
            break

        meal, product = line
        if len(shopping_dict[meal]) < meal_limits[meal]:
            shopping_dict[meal].add(product)

    for products in shopping_dict.values():
        if len(products) > 0:
            break
    else:
        return 'No products in the cart!'

    result = ''

    for meal, products in sorted(shopping_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f'{meal}:\n'
        for product in sorted(products):
            result += f' - {product}\n'

    return result


# Test code 1
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

# Test code 2
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# Test code 3
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
