def read_matrix():
    """
    Read size and rows of matrix
    """
    size = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(size)]


def find_diagonals(matrix):
    """
    Find the matrix's diagonals and their sum.
    """
    rows = len(matrix)

    primary = []
    secondary = []
    primary_sum = 0
    secondary_sum = 0
    for idx in range(rows):
        primary.append(matrix[idx][idx])
        primary_sum += matrix[idx][idx]
        secondary.append(matrix[idx][rows - idx - 1])
        secondary_sum += matrix[idx][rows - idx - 1]

    return primary, primary_sum, secondary, secondary_sum


matrix = read_matrix()
primary_diagonal, primary_diagonal_sum, secondary_diagonal, secondary_diagonal_sum = find_diagonals(matrix)
print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {secondary_diagonal_sum}')
