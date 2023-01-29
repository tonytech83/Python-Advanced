def read_matrix():
    """
    This function read new matrix from console and returns it.
    """
    size = 6
    new_matrix = []
    for row in range(size):
        new_matrix.append(input().split())

    return new_matrix


def execute_command(current_event: str, current_direction: str, row: int, col: int, current_value):
    """
    This function executes received command on received event and direction.
    """
    global matrix

    value = current_value[0] if current_value else None

    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1),
    }

    new_row, new_col = directions[current_direction]

    if current_event == CREATE:
        if matrix[new_row][new_col] == EMPTY_POSITION:
            matrix[new_row][new_col] = value

    elif current_event == UPDATE:
        if matrix[new_row][new_col] != EMPTY_POSITION:
            matrix[new_row][new_col] = value

    elif current_event == DELETE:
        matrix[new_row][new_col] = EMPTY_POSITION

    elif current_event == READ:
        if matrix[new_row][new_col] != EMPTY_POSITION:
            print(f'{matrix[new_row][new_col]}')

    return new_row, new_col


matrix = read_matrix()
start_row, start_col = [int(x) for x in input() if x.isdigit()]
EMPTY_POSITION = '.'
CREATE = 'Create'
UPDATE = 'Update'
DELETE = 'Delete'
READ = 'Read'
STOP = 'Stop'

while True:
    command = input()

    if command == STOP:
        break

    event, direction, *value = command.split(', ')

    start_row, start_col = execute_command(event, direction, start_row, start_col, value)

[print(*row, sep=' ') for row in matrix]
