def even_odd(*args):
    filter_command = args[-1]

    if filter_command == 'odd':
        return [x for x in args[:-1] if x % 2 != 0]
    else:
        return [x for x in args[:-1] if x % 2 == 0]


# Test code
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
