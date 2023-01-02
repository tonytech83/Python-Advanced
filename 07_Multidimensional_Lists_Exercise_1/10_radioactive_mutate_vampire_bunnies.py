from collections import deque


def find_stat():
    """
    Returns initial coordinates of player
    """
    for row_idx in range(len(lair)):
        current_row = lair[row_idx]
        for col_idx in range(len(current_row)):
            if lair[row_idx][col_idx] == 'P':
                return row_idx, col_idx


def bunnies_coordinates():
    """
    Returns coordinates of oll bunnies, before spread
    """
    all_bunnies = []
    for bunny_row in range(len(lair)):
        current_row = lair[bunny_row]
        for bunny_col in range(len(current_row)):
            if lair[bunny_row][bunny_col] == 'B':
                all_bunnies.append([bunny_row, bunny_col])

    return all_bunnies


def bunnies_spead(lair):
    """
    Receives all bunnies before spread and after every step made,
    each bunny spreads one position up, down, left, and right inside lair dimensions.
    """
    global is_death
    bunnies = bunnies_coordinates()

    for bunny_row, bunny_col in bunnies:
        potential_spread_cells = [
            [bunny_row, bunny_col - 1],  # left
            [bunny_row, bunny_col + 1],  # right
            [bunny_row - 1, bunny_col],  # up
            [bunny_row + 1, bunny_col],  # down
        ]

        for new_bunny_row, new_bunny_col in potential_spread_cells:
            if 0 <= new_bunny_row <= rows - 1 and 0 <= new_bunny_col <= cols - 1:
                if lair[new_bunny_row][new_bunny_col] == 'P':
                    is_death = True
                lair[new_bunny_row][new_bunny_col] = 'B'


def move(lair, new_move, p_row_idx, p_col_idx):
    """
    Moves player to new position related to received direction.
    """
    global is_death
    global is_winner

    directions = {
        'L': [p_row_idx, p_col_idx - 1],  # left
        'R': [p_row_idx, p_col_idx + 1],  # right
        'U': [p_row_idx - 1, p_col_idx],  # up
        'D': [p_row_idx + 1, p_col_idx],  # down
    }

    # new coordinates of player
    next_row, next_col = directions[new_move]

    # mark old position fo player with '.'
    lair[p_row_idx][p_col_idx] = '.'

    # check if player is outside of lair(matrix)
    if (next_row < 0 or next_row > rows - 1) or (next_col < 0 or next_col > cols - 1):
        is_winner = True
        return p_row_idx, p_col_idx

    # check if player moves to a bunny (cell with value 'B')
    if lair[next_row][next_col] == 'B':
        is_death = True
        return next_row, next_col

    # mark new coordinates of player with 'P'
    lair[next_row][next_col] = 'P'

    return next_row, next_col


# read rows and cols of lair (matrix) from console
rows, cols = [int(x) for x in input().split()]

# read lair (matrix) form console
lair = [[x for x in input()] for _ in range(rows)]

# read directions of moves from console
commands = deque(x for x in input())

is_death = False
is_winner = False

# coordinates of player
p_row_idx, p_col_idx = find_stat()

while commands:
    direction = commands.popleft()

    # coordinates of player after move
    p_row_idx, p_col_idx = move(lair, direction, p_row_idx, p_col_idx)

    # after every move spreads bunnies
    bunnies_spead(lair)

    if is_winner or is_death:
        break

for row in lair:
    print(*row, sep='')
if is_winner:
    print(f'won: {p_row_idx} {p_col_idx}')
else:
    print(f'dead: {p_row_idx} {p_col_idx}')
