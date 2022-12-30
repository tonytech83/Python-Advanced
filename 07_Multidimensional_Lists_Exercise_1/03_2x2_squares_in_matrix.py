def read_matrix(rows):
    """
    This func receives number of rows and reads from console rows separated by whitespace.
    """
    return [[x for x in input().split()] for _ in range(rows)]


def find_equal_squares(matrix, rows, cols):
    """
    This function searches the number of all 2x2 squares containing identical chars in a matrix.
    """
    equal_square = 0
    for row_idx in range(rows - 1):
        for col_idx in range(cols - 1):
            char_1 = matrix[row_idx][col_idx]
            char_2 = matrix[row_idx][col_idx + 1]
            char_3 = matrix[row_idx + 1][col_idx]
            char_4 = matrix[row_idx + 1][col_idx + 1]

            if char_1 == char_2 and char_1 == char_3 and char_1 == char_4:
                equal_square += 1

    return equal_square


rows, cols = [int(x) for x in input().split()]
matrix = read_matrix(rows)
print(find_equal_squares(matrix, rows, cols))
