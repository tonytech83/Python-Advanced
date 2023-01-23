def is_inside(row_idx, col_idx):
    """
    This func check if indexes are in matrix
    """
    return row_idx in range(len(matrix)) and col_idx in range(len(matrix))


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
COMMAND_END = 'END'
COMMAND_ADD = 'Add'
COMMAND_SUB = 'Subtract'

while True:
    command = input().split()
    if command[0] == COMMAND_END:
        break

    event, row, col, value = [int(x) if x.isdigit() else x for x in command]

    if not is_inside(row, col):
        print('Invalid coordinates')
    elif event == COMMAND_ADD:
        matrix[row][col] += value
    elif event == COMMAND_SUB:
        matrix[row][col] -= value

[print(*row, sep=' ') for row in matrix]
