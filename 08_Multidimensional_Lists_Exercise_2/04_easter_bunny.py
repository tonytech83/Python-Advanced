def find_bunny():
    """
    This func return row and col of 'B' in matrix.
    """
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'B':
                return [row, col]


def outside_or_x(row_idx, col_idx):
    """
    This func checks validity of new coordinates and the value of cell
    """
    return row_idx not in range(size) or col_idx not in range(size) or matrix[row_idx][col_idx] == 'X'


def move(row, col, direction):
    """
    This func saves paths and sums values for each visited cell per direction.
    At the end we have paths dict with row and col for each visited point in matrix and
    eggs dict which stores the sum of all values of points per location.
    """
    global paths
    global eggs

    directions = {
        'left': lambda r, c: (r, c - 1),
        'up': lambda r, c: (r - 1, c),
        'right': lambda r, c: (r, c + 1),
        'down': lambda r, c: (r + 1, c),
    }

    next_row, next_col = directions[direction](row, col)

    while not outside_or_x(next_row, next_col):
        paths[direction].append([next_row, next_col])

        if direction not in eggs:
            eggs[direction] = 0

        eggs[direction] += int(matrix[next_row][next_col])
        next_row, next_col = directions[direction](next_row, next_col)


def output():
    """
    This func prints:
    •	The direction which should be considered as best (lowercase)
    •	The field positions from which we are collecting eggs as lists
    •	The total number of eggs collected
    """
    max_path_value = max(eggs, key=eggs.get)

    print(max_path_value)
    [print(point) for point in paths[max_path_value]]
    print(eggs[max_path_value])


size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

bunny_row, bunny_col = find_bunny()

eggs = {}
paths = {
    'left': [],
    'up': [],
    'right': [],
    'down': [],
}

for direction in paths:
    move(bunny_row, bunny_col, direction)

output()
