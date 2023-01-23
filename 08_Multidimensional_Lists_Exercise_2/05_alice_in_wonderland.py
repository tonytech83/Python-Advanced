def is_outside(row_check, col_check):
    """
    Checks if indexes are outside wonderland(matrix).
    """
    return row_check not in range(size) or col_check not in range(size)


def is_rabit_hole(row_check, col_check):
    """
    Checks if coordinates are rabit hole
    """
    return wonderland[row_check][col_check] == 'R'


def move(row_idx, col_idx, direction):
    """
    Makes Alice from current coordinates to coordinates relative to received direction.
    """
    global dead_end
    global collected_bags

    directions = {
        'left': lambda r, c: (r, c - 1),
        'up': lambda r, c: (r - 1, c),
        'right': lambda r, c: (r, c + 1),
        'down': lambda r, c: (r + 1, c),
    }

    move_row, move_col = directions[direction](row_idx, col_idx)

    if is_outside(move_row, move_col):
        dead_end = True
    else:
        if is_rabit_hole(move_row, move_col):
            dead_end = True
        elif wonderland[move_row][move_col].isdigit():
            collected_bags += int(wonderland[move_row][move_col])

        wonderland[move_row][move_col] = '*'

    return move_row, move_col


def output():
    """
    This func prints requested result.
    """
    if collected_bags >= 10:
        print('She did it! She went to the party.')
    else:
        print("Alice didn't make it to the tea party.")

    [print(*row, sep=' ') for row in wonderland]


def read_wonderland():
    """
    Reads matrix from console and finds coordinates of Alice
    """
    matrix = []
    a_row = 0
    a_col = 0
    for row in range(size):
        row_elements = input().split()
        for col in range(size):
            if row_elements[col] == 'A':
                a_row = row
                a_col = col
        matrix.append(row_elements)
    return matrix, a_row, a_col


size = int(input())
wonderland, alice_row, alice_col = read_wonderland()
collected_bags = 0
dead_end = False
wonderland[alice_row][alice_col] = '*'

while True:

    if collected_bags >= 10 or dead_end:
        break

    command = input()
    alice_row, alice_col = move(alice_row, alice_col, command)

output()
