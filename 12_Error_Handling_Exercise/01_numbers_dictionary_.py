def error_message(error: str):
    """
    This func returns message regarding received error variable.
    """
    errors = {
        'ValueError': 'The variable number must be an integer',
        'KeyError': 'Number does not exist in dictionary',
    }

    return errors[error]


def main():
    """
    This func processes commands and data and returns a response or error based on received commands.
    """
    global numbers_dictionary

    while True:
        command = input()

        if command == SEARCH_COMMAND:
            break

        number = command

        try:
            digit = int(input())
            numbers_dictionary[number] = digit
        except ValueError:
            print(error_message(error='ValueError'))

    while True:
        command = input()

        if command == REMOVE_COMMAND:
            break

        wanted_number = command

        try:
            print(numbers_dictionary[wanted_number])
        except KeyError:
            print(error_message(error='KeyError'))

    while True:
        command = input()

        if command == END_COMMAND:
            print(numbers_dictionary)
            break

        number_to_remove = command

        try:
            del numbers_dictionary[number_to_remove]
        except KeyError:
            print(error_message(error='KeyError'))


numbers_dictionary = {}
SEARCH_COMMAND = 'Search'
REMOVE_COMMAND = 'Remove'
END_COMMAND = 'End'

main()
