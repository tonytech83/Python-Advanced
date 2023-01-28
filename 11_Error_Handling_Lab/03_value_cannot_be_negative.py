class ValueCannotBeNegative(Exception):
    """
    Number is below zero
    """
    pass


numbers = [int(input()) for _ in range(5)]

for num in numbers:
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative('The integer you provided is not a positive number')
