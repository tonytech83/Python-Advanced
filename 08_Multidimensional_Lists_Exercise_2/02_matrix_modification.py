def is_inside(row_idx, col_idx):
    """
    This func check if indexes are in matrix
    """
    return row_idx in range(len(matrix)) and col_idx in range(len(matrix))


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command = input().split()
    if command[0] == 'END':
        break

    row, col, value = [int(x) for x in command[1:]]

    if is_inside(row, col):
        if command[0] == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row, sep=' ')
