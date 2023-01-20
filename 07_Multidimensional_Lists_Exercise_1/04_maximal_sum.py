import sys


def read_matrix(rows):
    """
    Read matrix from console with rows size
    """
    return [[int(x) for x in input().split()] for _ in range(rows)]


def maximal_sum(matrix, rows, cols):
    """
    This func searches 3x3 submatrix with max sum of elements.
    """
    current_max_sum = -sys.maxsize
    biggest_submatrix = 0
    for row_idx in range(rows - 2):
        for col_idx in range(cols - 2):
            first_row = matrix[row_idx][col_idx:col_idx + 3]
            second_row = matrix[row_idx + 1][col_idx:col_idx + 3]
            third_row = matrix[row_idx + 2][col_idx:col_idx + 3]

            current_sum = sum(first_row) + sum(second_row) + sum(third_row)

            if current_sum > current_max_sum:
                current_max_sum = current_sum
                biggest_submatrix = [first_row, second_row, third_row]

    return current_max_sum, biggest_submatrix


# read rows and columns from console
rows, columns = [int(x) for x in input().split()]
matrix = read_matrix(rows)

max_sum, biggest_matrix = maximal_sum(matrix, rows, columns)

print(f'Sum = {max_sum}')
for row in biggest_matrix:
    print(*row, sep=' ')
