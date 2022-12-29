def read_matrix():
    """
    This func returns matrix with passed from console size and rows.
    """
    size = int(input())
    return [[int(s) for s in input().split()] for _ in range(size)]


def sum_primary_diagonal():
    """
    This func returns sum all numbers in primary diagonal of the matrix (matrix[0][0] + matrix[1][1] + ....)
    """
    return sum([matrix[idx][idx] for idx in range(len(matrix))])


# def sum_secondary_diagonal():
#     """
#     This func returns sum all numbers in secondary diagonal of the matrix.
#     The condition must be met: row_idx == len(matrix) - col_idx - 1
#     """
#     return sum([matrix[idx][len(matrix) - idx - 1] for idx in range(len(matrix))])


matrix = read_matrix()
print(sum_primary_diagonal())
# print(sum_secondary_diagonal())
