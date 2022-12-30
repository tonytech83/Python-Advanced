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
    max_sum = -sys.maxsize
    max_submatrix_start = 0
    for row in range(rows - 2):
        for col in range(cols - 2):
            current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                          matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                          matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

            if current_sum > max_sum:
                max_sum = current_sum
                max_submatrix_start = (row, col)

    return max_sum, max_submatrix_start


# read rows and columns from console
rows, columns = [int(x) for x in input().split()]
matrix = read_matrix(rows)

max_sum, max_submatrix_start = maximal_sum(matrix, rows, columns)
print(f'Sum = {max_sum}')
start_row = max_submatrix_start[0]
start_col = max_submatrix_start[1]
for row in range(3):
    for col in range(3):
        print(matrix[start_row + row][start_col + col], end=' ')
    print()
