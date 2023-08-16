"""
exam: 02. The Squirrel
url: https://judge.softuni.org/Contests/Practice/Index/3893#1
"""
from collections import deque


def is_inside(row, col):
    if row in range(size) and col in range(size):
        return True
    return False


def move_squirrel(squirrel_pos, move):
    global collected_hazelnuts
    global field
    global is_outside
    global is_trapped

    row, col = squirrel_pos

    moves_mapper = {
        "left": (row, col - 1),
        "right": (row, col + 1),
        "up": (row - 1, col),
        "down": (row + 1, col),
    }

    new_row, new_col = moves_mapper[move]

    if is_inside(new_row, new_col):
        if field[new_row][new_col] == HAZELNUT:
            collected_hazelnuts += 1
            field[new_row][new_col] = EMPTY
        elif field[new_row][new_col] == TRAP:
            is_trapped = True
    else:
        is_outside = True

    return new_row, new_col


size = int(input())
moves = deque(x for x in input().split(", "))

field = []
squirrel_pos = None
SQUIRREL, HAZELNUT, EMPTY, TRAP = "s", "h", "*", "t"

for row in range(size):
    line = input()

    if SQUIRREL in line:
        squirrel_pos = (row, line.index(SQUIRREL))

    field.append(list(line))

collected_hazelnuts = 0
is_outside = False
is_trapped = False

while moves:
    move = moves.popleft()

    squirrel_pos = move_squirrel(squirrel_pos, move)

    if is_outside or is_trapped:
        break

    if collected_hazelnuts == 3:
        break

if not is_outside and not is_trapped:
    if collected_hazelnuts < 3:
        print('There are more hazelnuts to collect.')
    else:
        print('Good job! You have collected all hazelnuts!')

if is_outside:
    print('The squirrel is out of the field.')

if is_trapped:
    print('Unfortunately, the squirrel stepped on a trap...')

print(f'Hazelnuts collected: {collected_hazelnuts}')
