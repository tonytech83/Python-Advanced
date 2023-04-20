from collections import deque


def math_operations(*args, **kwargs):
    """
    This function receives a different number of floats as arguments and 4 keyword arguments. The keys will be single
    letters: "a", "s", "d", "m", and the values will be numbers.
    Takes each float argument from the sequence and do mathematical operations as follows:
    •	The first element should be added to the value of the key "a"
    •	The second element should be subtracted from the value of the key "s"
    •	The third element should be divisor to the value of the key "d"
    •	The fourth element should be multiplied by the value of the key "m"
    •	Each result should replace the value of the corresponding key
    •	You must repeat the same steps consecutively until you run out of numbers
    """
    # define dict with all math operations

    operations = {
        'a': lambda a, b: a + b,
        's': lambda a, b: a - b,
        'd': lambda a, b: a / b if b != 0 else a,
        'm': lambda a, b: a * b,
    }

    # convert args tuple to deque
    numbers = deque(args)

    while numbers:
        for key, value in kwargs.items():
            if not numbers:
                break
            number = numbers.popleft()
            kwargs[key] = operations[key](kwargs[key], number)

    sorted_result = [f'{k}: {v:.1f}' for k, v in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))]

    return '\n'.join(sorted_result)


# Test codes
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
