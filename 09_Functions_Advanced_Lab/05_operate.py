from functools import reduce


def operate(sign, *args):
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    operations_map = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    return operations_map[sign](*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate('-', 2, 3, 3))
print(operate('/', 3, 4))


# Solution with reduce and eval
# def operate(sign, *args):
#     return reduce(lambda x, y: eval(f'{x} {sign} {y}'), args)
