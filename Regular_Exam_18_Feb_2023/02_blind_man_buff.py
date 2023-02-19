def create_playground():
    matrix = []
    player_coordinates = []

    for row in range(rows):
        matrix.append(input().split())
        if PLAYER in matrix[row]:
            player_coordinates = [row, matrix[row].index(PLAYER)]

    return matrix, player_coordinates


def is_inside(row, col):
    if row in range(rows) and col in range(columns):
        return True
    return False


def player_move(direction, current_coordinates):
    global playground
    global touched_opponents
    global total_moves

    row, col = current_coordinates

    directions = {
        'up': (row - 1, col),
        'down': (row + 1, col),
        'left': (row, col - 1),
        'right': (row, col + 1),
    }

    new_row, new_col = directions[direction]

    if is_inside(new_row, new_col):
        if playground[new_row][new_col] == OBSTACLE:
            return row, col

        elif playground[new_row][new_col] == OTHER_PLAYER:
            touched_opponents += 1
            total_moves += 1

        elif playground[new_row][new_col] == EMPTY:
            total_moves += 1

        playground[row][col] = EMPTY
        playground[new_row][new_col] = PLAYER
        return new_row, new_col

    else:
        return row, col


rows, columns = [int(x) for x in input().split()]

PLAYER, OBSTACLE, OTHER_PLAYER, EMPTY, COMMAND_FINISH = 'B', 'O', 'P', '-', 'Finish'
total_moves = 0
touched_opponents = 0

playground, player = create_playground()

while touched_opponents < 3:
    command = input()

    if command == COMMAND_FINISH:
        break

    player = player_move(command, player)

print(f'Game over!\nTouched opponents: {touched_opponents} Moves made: {total_moves}')
