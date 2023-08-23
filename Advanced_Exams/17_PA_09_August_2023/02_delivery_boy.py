"""
exam: 02. Delivery Boy
judge: https://judge.softuni.org/Contests/Practice/Index/4089#1
"""


def is_inside(row, col):
    return row in range(rows) and col in range(cols)


def move(position, direction):
    global is_outside
    global is_pizza_collected
    global is_pizza_delivered
    global field

    row, col = position

    direction_mapper = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'right': (row, col + 1),
        'left': (row, col - 1)
    }

    new_row, new_col = direction_mapper[direction]

    if is_inside(new_row, new_col):
        if field[new_row][new_col] == RESTAURANT:
            field[new_row][new_col] = 'R'
            is_pizza_collected = True
        elif field[new_row][new_col] == OBSTACLE:
            return row, col
        elif field[new_row][new_col] == ADDRESS:
            is_pizza_delivered = True
            field[new_row][new_col] = 'P'
        elif field[new_row][new_col] == ROAD:
            field[new_row][new_col] = '.'
    else:
        is_outside = True

    return new_row, new_col


START, ADDRESS, OBSTACLE, RESTAURANT, ROAD = 'B', 'A', '*', 'P', '-'
rows, cols = [int(x) for x in input().split()]
field = []
start_pos = tuple()

for row in range(rows):
    field.append([x for x in input()])
    if START in field[row]:
        start_pos = (row, field[row].index(START))

initial_pos = start_pos
is_pizza_collected = False
is_pizza_delivered = False
is_outside = False

while True:
    command = input()

    start_pos = move(start_pos, command)

    if is_outside:
        field[initial_pos[0]][initial_pos[1]] = ' '
        print('The delivery is late. Order is canceled.')
        break

    if is_pizza_collected:
        is_pizza_collected = False
        print('Pizza is collected. 10 minutes for delivery.')

    if is_pizza_delivered:
        print('Pizza is delivered on time! Next order...')
        break

[print(''.join(row)) for row in field]
