# Exam: 02. Checkmate
# From: Python Advanced Exam - 24 October 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2551#1

from collections import deque


def create_chessboard():
    """
    Create chessboard and collect coordinates for all queens marked with 'Q' in deque.
    """
    matrix = []
    queens_coordinates = deque()

    for row in range(SIZE):
        matrix.append(input().split())

        if QUEEN in matrix[row]:
            for col in range(len(matrix[row])):
                if matrix[row][col] == QUEEN:
                    queens_coordinates.append([row, col])

    return matrix, queens_coordinates


def is_inside(row, col):
    """
    Checks if new coordinates are inside chessboard.
    """
    if row in range(SIZE) and col in range(SIZE):
        return True
    return False


def move_queen(row, col, direction):
    """
    Moves the queen relative to the received direction during:
    - go outside of chessboard
    - hit other queen
    - hit the King
    """
    global bad_queens

    row += direction[0]
    col += direction[1]

    if is_inside(row, col):
        if chessboard[row][col] == KING:
            bad_queens.append(current_queen)
            return
        elif chessboard[row][col] == QUEEN:
            return
    else:
        return

    move_queen(row, col, direction)


def check_for_bad_queen(coordinates):
    """
    Takes coordinates of the current queen and tries to move it diagonally, horizontally and vertically.
    """
    row, col = coordinates

    directions = {
        'up': (-1, 0),
        'down': (+1, 0),
        'left': (0, -1),
        'right': (0, +1),
        'upleft': (+1, -1),
        'upright': (+1, +1),
        'downleft': (-1, -1),
        'downright': (-1, +1),
    }

    for direction in directions:
        move_queen(row, col, directions[direction])


def output():
    if bad_queens:
        print(*bad_queens, sep='\n')
    else:
        print('The king is safe!')


QUEEN = 'Q'
SIZE = 8
KING = 'K'
chessboard, queens = create_chessboard()
bad_queens = []

while queens:
    current_queen = queens.popleft()
    check_for_bad_queen(current_queen)

output()
