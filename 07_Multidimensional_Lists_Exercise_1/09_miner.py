from collections import deque


def find_stat():
    """
    Find initial start position
    """
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == 's':
                return row_idx, col_idx


def move(start_row: int, start_col: int, direction: str, matrix: list):
    """
    This func returns new position after performed move relative to the obtained coordinates.
    """
    global game_over
    global coals

    # dict with all coordinates according to received direction
    directions = {
        'left': [start_row, start_col - 1],
        'right': [start_row, start_col + 1],
        'up': [start_row - 1, start_col],
        'down': [start_row + 1, start_col],
    }

    row_idx, col_idx = directions[direction]

    # check if new coordinates are valid, if not returns start position
    if row_idx not in range(size) or col_idx not in range(size):
        return start_row, start_col

    elif matrix[row_idx][col_idx] == 'c':
        matrix[row_idx][col_idx] = '*'
        coals -= 1

    elif matrix[row_idx][col_idx] == 'e':
        game_over = True

    return row_idx, col_idx


size = int(input())
commands = deque(x for x in input().split())
matrix = [[x for x in input().split()] for _ in range(size)]

# take quantity af coals in our matrix
coals = sum([row.count('c') for row in matrix])

game_over = False
start_row, start_col = find_stat()

while commands:

    direction = commands.popleft()

    start_row, start_col = move(start_row, start_col, direction, matrix)

    if game_over:
        print(f'Game over! ({start_row}, {start_col})')
        break

    if coals == 0:
        print(f'You collected all coal! ({start_row}, {start_col})')
        break

if coals > 0 and not game_over:
    print(f'{coals} pieces of coal left. ({start_row}, {start_col})')
