def grocery_store(**kwargs):
    """
    Return a sorted receipt for all products. They should be sorted by their quantity in descending order. If there are
    two or more products with the same quantity, sort them by their name's length in descending order. If there are two
    or more products with the same name's length, sort them by their name in ascending order (alphabetically)
    """
    sorted_grocery = [f'{name}: {quantity}' for name, quantity in
                      sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))]
    return '\n'.join(sorted_grocery)


# Test code 1
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

# Test code 2
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
