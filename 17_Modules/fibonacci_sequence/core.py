from .helper import create_fib_seq, locate_number
from .print_result import output


def run_fib():
    """
    Main logic of program.
    """
    sequence = []
    while True:
        data = input()

        if data == 'Stop':
            break

        split_data = data.split()

        if split_data[0] == 'Create':
            number = int(split_data[-1])
            sequence = create_fib_seq(number)
            print(*sequence)

        if split_data[0] == 'Locate':
            if sequence:
                number = int(split_data[-1])
                try:
                    index = locate_number(sequence, number)
                    # print(f'The number - {number} is at index {index}')
                    output(number, index)
                except ValueError:
                    # print(f'The number {number} is not in the sequence')
                    output(number, idx=False)
