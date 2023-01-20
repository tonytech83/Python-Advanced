def read_matrix(rows):
    """
    This func receives number of rows and reads from console elements separated by whitespace.
    """
    return [input().split() for _ in range(rows)]


def find_equal_squares(matrix, rows, cols):
    """
    This function searches the number of all 2x2 squares containing identical chars in the matrix.
    """
    equal_square = 0
    for row_idx in range(rows - 1):
        for col_idx in range(cols - 1):
            symbol = matrix[row_idx][col_idx]
            symbol_right = matrix[row_idx][col_idx + 1]
            symbol_down = matrix[row_idx + 1][col_idx]
            symbol_right_down = matrix[row_idx + 1][col_idx + 1]

            # check if all chars are identical
            if symbol == symbol_right == symbol_down == symbol_right_down:
                equal_square += 1

    return equal_square


rows, cols = [int(x) for x in input().split()]
matrix = read_matrix(rows)
print(find_equal_squares(matrix, rows, cols))
