def read_matrix():
    """
    This func reads rows and columns from console, after that reads elements of columns and store them in list of lists.
    """
    rows, columns = [int(x) for x in input().split(', ')]

    current_matrix = []

    for _ in range(rows):
        elements = [int(x) for x in input().split(', ')]
        current_matrix.append(elements)

    return current_matrix


matrix = read_matrix()

sum_matrix_elements = 0
for row in matrix:
    sum_matrix_elements += sum(row)

print(sum_matrix_elements)
print(matrix)
