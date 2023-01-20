def read_matrix():
    """
    Read size and rows of matrix
    """
    size = int(input())
    return [[int(x) for x in input().split()] for _ in range(size)]


def diagonals_difference():
    """
    Find the absolute difference between the primary and the secondary diagonal sums.
    """
    rows = len(matrix)

    primary_sum = sum([matrix[idx][idx] for idx in range(rows)])
    secondary_sum = sum([matrix[idx][rows - idx - 1] for idx in range(rows)])

    return abs(primary_sum - secondary_sum)


matrix = read_matrix()
print(diagonals_difference())
