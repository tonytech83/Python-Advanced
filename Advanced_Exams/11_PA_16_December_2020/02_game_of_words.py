# Exam: 02. Game of Words
# From: Python Advanced Retake Exam - 16 December 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2720#1

def create_field(size):
    """
    Creates filed with input from console and takes the coordinates of player.
    """
    matrix = []
    player_start_coordinates = []

    for row in range(size):
        matrix.append([x for x in input()])
        if PLAYER in matrix[row]:
            player_start_coordinates.append(row)
            player_start_coordinates.append(matrix[row].index(PLAYER))

    return matrix, player_start_coordinates


def inside(row, col):
    """
    Checks if new coordinates are inside field.
    """
    if row in range(size) and col in range(size):
        return True
    return False


def player_move(coordinates, direction):
    """
    Move player and checks his new position.
    """
    global filed
    global text

    row, col = coordinates

    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1)
    }

    new_row, new_col = directions[direction]

    if inside(new_row, new_col):
        text += filed[new_row][new_col] if filed[new_row][new_col].isalpha() else ''
        filed[row][col] = EMPTY_POSITION
        filed[new_row][new_col] = PLAYER
        return new_row, new_col
    else:
        text = text[:-1]
        return row, col


text = input()
size = int(input())
PLAYER = 'P'
EMPTY_POSITION = '-'

filed, player_coordinates = create_field(size)

commands_count = int(input())

for _ in range(commands_count):
    command = input()

    player_coordinates = player_move(player_coordinates, command)

print(text)
[print(*row, sep='') for row in filed]
