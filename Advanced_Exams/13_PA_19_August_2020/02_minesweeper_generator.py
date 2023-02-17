# Exam: 02. Minesweeper Generator
# From: Python Advanced Retake Exam - 19 August 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2463#1

from collections import deque


def create_filed():
    """
    Creates field and place all mines
    """
    matrix = [[0] * size for _ in range(size)]

    for mine in mines_coordinates:
        matrix[mine[0]][mine[1]] = MINE

    return matrix


def is_inside(row, col):
    """
    Checks child cell is inside field
    """
    if row in range(size) and col in range(size):
        return True
    return False


def numbers_around_mine(mine):
    """
    Increases the value in each cell of the field around the current mine.
    """
    global field

    childs = {
        'up': (-1, 0),
        'down': (+1, 0),
        'left': (0, -1),
        'right': (0, +1),
        'upleft': (+1, -1),
        'upright': (+1, +1),
        'downleft': (-1, -1),
        'downright': (-1, +1),
    }

    for child in childs:
        row, col = mine[0] + childs[child][0], mine[1] + childs[child][1]
        if is_inside(row, col) and isinstance(field[row][col], int):
            field[row][col] += 1


size = int(input())
bombs_count = int(input())
MINE = '*'
mines_coordinates = deque(eval(input()) for _ in range(bombs_count))

field = create_filed()

while mines_coordinates:
    current_mine = mines_coordinates.popleft()

    numbers_around_mine(current_mine)

[print(*row, sep=' ') for row in field]
