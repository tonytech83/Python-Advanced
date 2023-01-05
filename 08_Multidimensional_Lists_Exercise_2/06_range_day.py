def read_matrix():
    """
    Reads console input and returns battle filed, targets count(all cells with value 'x'),
    and coordinates of cell with value 'A'.
    """
    row_idx = 0
    col_idx = 0
    matrix = []
    targets_count = 0

    for row in range(SIZE):
        row_elements = input().split()
        targets_count += row_elements.count('x')
        for col in range(SIZE):
            if row_elements[col] == 'A':
                row_idx = row
                col_idx = col
        matrix.append(row_elements)

    return matrix, targets_count, row_idx, col_idx


def is_inside(row, col):
    """
    Checks received indexes are valid (inside field).
    """
    return row in range(SIZE) and col in range(SIZE)


def moving(row, col, direct, with_step):
    """
    Moves the solder inside matrix according to the given direction and step.
    """
    global field

    directions = {
        'left': lambda r, c: (r, c - with_step),
        'up': lambda r, c: (r - with_step, c),
        'right': lambda r, c: (r, c + with_step),
        'down': lambda r, c: (r + with_step, c),
    }

    row_idx, col_idx = directions[direct](row, col)

    if is_inside(row_idx, col_idx) and field[row_idx][col_idx] == '.':
        return row_idx, col_idx
    return row, col


def shooting(row, col, direct):
    """
    Shot the first target encountered.
    """
    global field
    global targets_shot
    global targets

    directions = {
        'left': lambda r, c: (r, c - 1),
        'up': lambda r, c: (r - 1, c),
        'right': lambda r, c: (r, c + 1),
        'down': lambda r, c: (r + 1, c),
    }

    row_idx, col_idx = directions[direct](row, col)

    if is_inside(row_idx, col_idx):
        if field[row_idx][col_idx] == 'x':
            field[row_idx][col_idx] = '.'
            targets -= 1
            targets_shot.append([row_idx, col_idx])
        else:
            shooting(row_idx, col_idx, direct)


def output():
    """
    Prints final result according left targets.
    """
    if targets == 0:
        print(f'Training completed! All {len(targets_shot)} targets hit.')
    else:
        print(f'Training not completed! {targets} targets left.')
    print(*targets_shot, sep='\n')


SIZE = 5
field, targets, solder_row, solder_col = read_matrix()

targets_shot = []
n = int(input())
field[solder_row][solder_col] = '.'

for _ in range(n):
    instruction = input().split()
    event = instruction[0]
    direction = instruction[1]

    if event == 'move':
        steps = int(instruction[2])
        solder_row, solder_col = moving(solder_row, solder_col, direction, steps)
    else:
        shooting(solder_row, solder_col, direction)

    if targets == 0:
        break

output()
