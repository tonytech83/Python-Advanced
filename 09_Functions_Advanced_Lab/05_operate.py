def operate(sign, *args):
    def add(*args):
        return sum(x for x in args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for num in args:
            result *= num

        return result

    def divide(x, *args):
        result = x
        for num in args:
            result /= num

        return result

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
