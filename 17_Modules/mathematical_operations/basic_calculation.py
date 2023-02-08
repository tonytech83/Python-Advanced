def calculation(number_1, sign, number_2):
    operations = {
        '/': lambda a, b: a / b,
        '*': lambda a, b: a * b,
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b,
        '^': lambda a, b: a ** b,
    }

    try:
        return f'{operations[sign](float(number_1), float(number_2)):.2f}'
    except ZeroDivisionError:
        return 'You can not divide by zero!'


def print_result(number_1, sign, number_2):
    print(calculation(number_1, sign, number_2))
