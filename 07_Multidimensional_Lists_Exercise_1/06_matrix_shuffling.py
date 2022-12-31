def read_matrix(rows):
    """
    Read matrix from console input.
    """
    return [[x for x in input().split()] for _ in range(rows)]


def valid_indexes(command):
    """
    Checks if coordinates are digits and are inside matrix.
    """
    row1, col1, row2, col2 = [x for x in command[1:]]
    if row1.isdigit() and col1.isdigit() and row2.isdigit() and col2.isdigit():
        if int(row1) < rows and int(row2) < rows and int(col1) < columns and int(col2) < columns:
            return True
    return False


def valid_format(command):
    """
    Check if command is in valid format (contains 5 elements).
    """
    if len(command) == 5:
        return True
    return False


rows, columns = [int(x) for x in input().split()]
matrix = read_matrix(rows)

while True:
    command = input().split()
    if command[0] == 'END':
        break

    if command[0] != 'swap' or not valid_format(command):
        print('Invalid input!')
        continue

    if valid_indexes(command):
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = \
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
        for row in matrix:
            print(*row, sep=' ')
    else:
        print('Invalid input!')
