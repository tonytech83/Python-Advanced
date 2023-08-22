"""
exam: 02. Mouse In The Kitchen
url: https://judge.softuni.org/Contests/Practice/Index/4081#1
"""


def is_inside(row, col):
    if row in range(rows) and col in range(cols):
        return True
    return False


def move_mouse(position, direction):
    global is_outside
    global is_trapped
    global matrix
    global cheeses

    row, col = position

    directions_mapper = {
        "left": (row, col - 1),
        "right": (row, col + 1),
        "up": (row - 1, col),
        "down": (row + 1, col),
    }

    new_row, new_col = directions_mapper[direction]

    if is_inside(new_row, new_col):
        if matrix[new_row][new_col] == CHEESE:
            cheeses -= 1
            matrix[new_row][new_col] = MOUSE
            matrix[row][col] = EMPTY
            return new_row, new_col
        if matrix[new_row][new_col] == TRAP:
            matrix[row][col] = EMPTY
            matrix[new_row][new_col] = MOUSE
            is_trapped = True
        if matrix[new_row][new_col] == WALL:
            return row, col
        if matrix[new_row][new_col] == EMPTY:
            matrix[row][col] = EMPTY
            matrix[new_row][new_col] = MOUSE
            return new_row, new_col

    else:
        is_outside = True


MOUSE, CHEESE, EMPTY, WALL, TRAP = 'M', 'C', '*', '@', 'T'

rows, cols = [int(x) for x in input().split(',')]

matrix = []
mouse_pos = ()
is_outside = False
is_trapped = False
cheeses = 0

for row in range(rows):
    matrix.append(list(input()))
    if MOUSE in matrix[row]:
        mouse_pos = (row, matrix[row].index(MOUSE))
    cheeses += matrix[row].count(CHEESE)

while True:
    command = input()

    if command == 'danger':
        break

    mouse_pos = move_mouse(mouse_pos, command)

    if is_outside:
        print('No more cheese for tonight!')
        break

    if cheeses == 0:
        print('Happy mouse! All the cheese is eaten, good night!')
        break

    if is_trapped:
        print('Mouse is trapped!')
        break

if cheeses and command == 'danger':
    print('Mouse will come back later!')

[print(''.join(row)) for row in matrix]
