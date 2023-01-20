def read_matrix():
    """
    Read size of square matrix and returns read from console rows by received size.
    """
    size = int(input())
    return [[int(x) for x in input().split(', ')] for _ in range(size)]


def find_diagonals(matrix):
    """
    Find the matrix's diagonals and returns them in two lists.
    """
    rows = len(matrix)

    primary = [matrix[idx][idx] for idx in range(rows)]
    secondary = [matrix[idx][rows - idx - 1] for idx in range(rows)]

    return primary, secondary


matrix = read_matrix()
primary_diagonal, secondary_diagonal = find_diagonals(matrix)
print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
