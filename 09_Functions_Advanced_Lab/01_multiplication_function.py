# from functools import reduce


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
    # The code in function can be replaced with reduce!!! To use reduce should import reduce from functools
    # return reduce(lambda a, b: a * b, args)


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
