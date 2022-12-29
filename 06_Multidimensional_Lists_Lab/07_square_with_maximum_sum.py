import sys


def find_max_submatrix(matrix):
    max_sum = - sys.maxsize
    max_submatrix = []
    for row_idx in range(len(matrix) - 1):
        for col_idx in range(len(matrix[row_idx]) - 1):
            submatrix_sum = matrix[row_idx][col_idx] + matrix[row_idx][col_idx + 1] + \
                            matrix[row_idx + 1][col_idx] + matrix[row_idx + 1][col_idx + 1]

            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [[matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1]],
                                 [matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1]]]

    return max_submatrix, max_sum


# read matrix size from console
rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

# Find the 2x2 submatrix with the greatest sum
max_submatrix, max_sum = find_max_submatrix(matrix)

# Print the found submatrix and its sum
for row in max_submatrix:
    print(*row, sep=' ')
print(max_sum)
