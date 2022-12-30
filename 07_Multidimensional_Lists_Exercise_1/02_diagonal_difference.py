def read_matrix():
    """
    Read size and rows of matrix
    """
    size = int(input())
    return [[int(x) for x in input().split()] for _ in range(size)]


def diagonals_difference(matrix):
    """
    Find the absolute difference between the primary and the secondary diagonal sums.
    """
    rows = len(matrix)

    primary_sum = 0
    secondary_sum = 0
    for idx in range(rows):
        primary_sum += matrix[idx][idx]
        secondary_sum += matrix[idx][rows - idx - 1]

    return abs(primary_sum - secondary_sum)


matrix = read_matrix()
print(diagonals_difference(matrix))
