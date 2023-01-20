def read_matrix(rows):
    """
    Read matrix from console input.
    """
    return [[x for x in input().split()] for _ in range(rows)]


def valid_indexes(indexes):
    """
    Checks if coordinates are digits and are inside matrix.
    """
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols):
        return True

    return False


def valid_format(indexes):
    """
    Check if receive 4 indexes.
    """
    if len(indexes) == 4:
        return True

    return False


rows, columns = [int(x) for x in input().split()]
matrix = read_matrix(rows)
valid_rows = range(rows)
valid_cols = range(columns)

while True:
    event, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if event == 'END':
        break

    if event != 'swap' or not valid_format(data):
        print('Invalid input!')
        continue

    if valid_indexes(data):
        matrix[int(data[0])][int(data[1])], matrix[int(data[2])][int(data[3])] = \
            matrix[int(data[2])][int(data[3])], matrix[int(data[0])][int(data[1])]
        for row in matrix:
            print(*row, sep=' ')
    else:
        print('Invalid input!')
