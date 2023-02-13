def read_battlefield():
    """
    This func read matrix from console and returns the matrix and coordinates of element 'S'.
    """
    size = int(input())
    matrix = []
    coordinates = ()

    for row in range(size):
        matrix.append([x for x in input()])
        if 'S' in matrix[row]:
            coordinates = (row, matrix[row].index('S'))

    return matrix, coordinates


def submarine_move(row, col, direction):
    """
    This func returns new position of submarine relative to received direction.
    """
    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1),
    }

    next_row, next_col = directions[direction]

    return next_row, next_col


battlefield, submarine_coordinates = read_battlefield()
battle_cruisers = 3
blown_mines = 0
MINE = '*'
CRUISER = 'C'
EMPTY_FIELD = '-'
SUBMARINE = 'S'

submarine_row, submarine_col = submarine_coordinates

while battle_cruisers:
    # received from console direction
    direction = input()

    # mark old position of submarine as EMPTY_FIELD
    battlefield[submarine_row][submarine_col] = EMPTY_FIELD

    submarine_row, submarine_col = submarine_move(submarine_row, submarine_col, direction)

    if battlefield[submarine_row][submarine_col] == MINE:
        blown_mines += 1

    elif battlefield[submarine_row][submarine_col] == CRUISER:
        battle_cruisers -= 1

    # mark the new position of submarine with 'S'
    battlefield[submarine_row][submarine_col] = SUBMARINE

    if blown_mines == 3:
        break

if battle_cruisers == 0:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
else:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!')

[print(*row, sep='') for row in battlefield]
