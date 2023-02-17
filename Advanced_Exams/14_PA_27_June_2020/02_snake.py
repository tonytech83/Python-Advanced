# Exam: 02. Snake
# From: Python Advanced Exam - 27 June 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2456#1

def create_territory():
    snake_territory = []
    snake_coordinates = []
    burrows_coordinates = []

    for row in range(size):
        snake_territory.append([x for x in input()])

        if SNAKE in snake_territory[row]:
            snake_coordinates.append(row)
            snake_coordinates.append(snake_territory[row].index(SNAKE))

        if BURROW in snake_territory[row]:
            burrows_coordinates.append([row, snake_territory[row].index(BURROW)])

    return snake_territory, snake_coordinates, burrows_coordinates


def is_inside(row, col):
    if row in range(size) and col in range(size):
        return True
    return False


def move_snake(snake_coordinates, direction):
    global territory
    global is_outside
    global eaten_food

    row, col = snake_coordinates

    territory[row][col] = TRAIL

    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1),
    }

    new_row, new_col = directions[direction]

    if is_inside(new_row, new_col):
        if territory[new_row][new_col] == FOOD:
            eaten_food += 1
            territory[new_row][new_col] = SNAKE
        elif territory[new_row][new_col] == BURROW:
            territory[new_row][new_col] = TRAIL
            new_row, new_col = burrows[1] if [new_row, new_col] == burrows[0] else burrows[0]
            territory[new_row][new_col] = SNAKE
        else:
            territory[new_row][new_col] = SNAKE
    else:
        is_outside = True

    return new_row, new_col


eaten_food = 0
size = int(input())
SNAKE, BURROW, FOOD, EMPTY, TRAIL = 'S', 'B', '*', '-', '.'
territory, snake_cell, burrows = create_territory()
is_outside = False

while True:
    command = input()

    snake_cell = move_snake(snake_cell, command)

    if is_outside or eaten_food == 10:
        break

print(f'Game over!\nFood eaten: {eaten_food}' if is_outside else 'You won! You fed the snake.\nFood eaten: 10')
[print(*row, sep='') for row in territory]
