class ValueCannotBeNegative(Exception):
    """
    Number is below zero
    """
    pass


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative('The integer you provided is not a positive number')
