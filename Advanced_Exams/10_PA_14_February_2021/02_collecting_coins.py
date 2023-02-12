# Exam: 02. Collecting Coins
# From: Python Advanced Exam - 14 February 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2812#1
def create_field():
    """
    This func creates field and found coordinates of player.
    """
    matrix = []
    player_row = 0
    player_col = 0

    for row in range(size):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
        if 'P' in matrix[row]:
            player_row = row
            player_col = matrix[row].index('P')

    return matrix, player_row, player_col


def move_player(row: int, col: int, direction):
    """
    This func moves player on field and increases the collected coins.
    Returns new position of player
    """
    global collected_coins
    global field
    global hit_wall

    directions = {
        'up': [row - 1, col],
        'down': [row + 1, col],
        'left': [row, col - 1],
        'right': [row, col + 1]
    }

    next_row, next_col = directions[direction]

    # if row or col goes outside of field, player continue from the opposite side in the same direction
    next_row = 0 if next_row > size - 1 else next_row
    next_col = 0 if next_col > size - 1 else next_col
    next_row = size - 1 if next_row < 0 else next_row
    next_col = size - 1 if next_col < 0 else next_col

    if isinstance(field[next_row][next_col], int):
        collected_coins += field[next_row][next_col]
        field[next_row][next_col] = VISITED

    elif field[next_row][next_col] == WALL:
        hit_wall = True

    return next_row, next_col


def output():
    """
    This func prints success/not success regarding hit_wall boolean and path of player.
    """
    if hit_wall:
        print(f"Game over! You've collected {int(collected_coins * 0.5)} coins.")
    else:
        print(f"You won! You've collected {collected_coins} coins.")

    print('Your path:')
    [print(position) for position in path]


def main(player_coordinates):
    """
    Mian func which receives the command with direction for player and observes for the occurrence of hit_wall or
    collected point at least 100.
    """
    global path

    row, col = player_coordinates

    while True:
        path.append(f'[{row}, {col}]')
        command = input()

        row, col = move_player(row, col, command)

        if hit_wall or collected_coins >= 100:
            path.append(f'[{row}, {col}]')
            output()
            break


collected_coins = 0
path = []
hit_wall = False
WALL = 'X'
VISITED = 'V'
size = int(input())
field, *coordinates = create_field()

main(coordinates)
