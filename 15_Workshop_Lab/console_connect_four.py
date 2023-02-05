class InvalidColumnError(Exception):
    """
    Raise a custom error when the received column is out of the playground.
    """
    pass


class FullColumnError(Exception):
    """
    Raise a custom error when the received column is already filled.
    """
    pass


def read_playground(rows: int, cols: int):
    """
    This func creates playground from received rows and cols and fill it with zeroes.
    """
    matrix = []

    for _ in range(rows):
        matrix.append([0] * cols)

    return matrix


def place_player_choice(choice: int, current_player: int):
    """
    Place player marker on selected column.
    If column is full ask same player to choose other column.
    """
    global playground

    start_row = playground_rows - 1
    for row_idx in range(start_row, -1, -1):
        if playground[row_idx][choice] == ZERO:
            playground[row_idx][choice] = current_player
            return row_idx
    else:
        raise FullColumnError


def check_for_player_num(row: int, col: int, player_numer: int):
    """
    This func returns True if received coordinates are valid and not equal to 0.
    """
    if col < 0 or row < 0:
        return 0
    try:
        if playground[row][col] == player_numer:
            return True
    except IndexError:
        return False
    return False


def check_horizontal(row: int, col: int, current_player: int, winning_count: int):
    """
    Checks horizontal from marked cell for current player number.
    """
    right = []
    for idx in range(winning_count):
        if check_for_player_num(row, col + idx, current_player):
            right.append(True)
        else:
            break

    left = []
    for idx in range(winning_count):
        if check_for_player_num(row, col + idx, current_player):
            left.append(True)
        else:
            break

    return len(right + left) > winning_count


def check_vertical(row: int, col: int, current_player: int, winning_count: int):
    """
    Checks vertical from marked cell for current player number.
    Should not checks up because we can't mark cell if above cell have already marked.
    """

    # up = all([check_for_player_num(row - idx, col, current_player) for idx in range(winning_count)])
    down = all([check_for_player_num(row + idx, col, current_player) for idx in range(winning_count)])

    return down


def check_primary_diagonal(row: int, col: int, current_player: int, winning_count: int):
    """
    Checks primary diagonal from marked cell for current player number.
    """
    # TODO -> same as horizontal
    left_up = [check_for_player_num(row - idx, col - idx, current_player) for idx in range(winning_count)].count(True)
    right_down = [check_for_player_num(row + idx, col + idx, current_player) for idx in range(winning_count)].count(
        True)

    return (left_up + right_down) > winning_count


def check_secondary_diagonal(row: int, col: int, current_player: int, winning_count: int):
    """
    Checks secondary diagonal from marked cell for current player number.
    """
    # TODO -> same as horizontal
    right_up = [check_for_player_num(row - idx, col + idx, current_player) for idx in range(winning_count)].count(True)
    left_down = [check_for_player_num(row + idx, col - idx, current_player) for idx in range(winning_count)].count(True)

    return (right_up + left_down) > winning_count


def check_for_win(row: int, col: int, current_player: int, winning_count=4):
    """
    This func receives row and col which represents last market position, current player and count of cells for winning.
    Tries all directions for same value as current player number (1 or 2).
    If any of checked directions returns True, we have a winner.

    """
    horizontal = check_horizontal(row, col, current_player, winning_count)
    vertical = check_vertical(row, col, current_player, winning_count)
    primary_diagonal = check_primary_diagonal(row, col, current_player, winning_count)
    secondary_diagonal = check_secondary_diagonal(row, col, current_player, winning_count)

    if any([horizontal, vertical, primary_diagonal, secondary_diagonal]):
        return True
    return False


def validate_column_choice(selected_column: int, max_column: int):
    """
    Verifies player choice of column is valid, if not same player tries again.
    """
    if not (0 <= selected_column <= max_column):
        raise InvalidColumnError


def print_playground():
    """
    Prints playground after player turn.
    """
    [print(row) for row in playground]


playground_rows = 6
playground_cols = 7
ZERO = 0
playground = read_playground(playground_rows, playground_cols)

player_number = 1
while True:

    player_number = 2 if player_number % 2 == 0 else 1

    try:
        chosen_column = int(input(f'Player {player_number}, please choose a column: ')) - 1
        validate_column_choice(chosen_column, playground_cols - 1)
        cell_row = place_player_choice(chosen_column, player_number)
        print_playground()
        if check_for_win(cell_row, chosen_column, player_number):
            print(f'The winner is player {player_number}')
            break
    except InvalidColumnError:
        print(f'This column is not valid! Please choose between 1 and {playground_cols}')
        continue
    except ValueError:
        print('Please select valid digit!')
        continue
    except FullColumnError:
        print(f'Selected column is already full! Please choose different column.')
        continue

    # If the turn was successful, next player turn
    player_number += 1
