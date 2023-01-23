def inside(row_idx: int, col_idx: int):
    """
    This function check if move is inside board(matrix).
    """
    return row_idx in range(size) and col_idx in range(size)


def remove_knight(max_key: str):
    """
    This func removes knight with most hits
    """
    global board
    global removed_knights

    row_idx, col_idx = [int(x) for x in max_key.split()]
    board[row_idx][col_idx] = 0
    removed_knights += 1


def check_hits():
    """
    This function finds knight with most hits, repeat the func till don't have knight with hits at all.
    """
    global we_are_ready
    global removed_knights

    knights_hits = {}

    for row in range(size):
        for col in range(size):
            # all possible moves of knight in chess
            possible_moves = (
                (row - 1, col - 2),
                (row - 2, col - 1),
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2)
            )

            hits = 0
            if board[row][col] == 'K':
                for child_row, child_col in possible_moves:
                    if inside(child_row, child_col) and board[child_row][child_col] == 'K':
                        hits += 1

            if hits > 0:
                knights_hits[f'{row} {col}'] = hits

    if knights_hits:
        key_of_max_value = max(knights_hits, key=knights_hits.get)
        remove_knight(key_of_max_value)
    else:
        we_are_ready = True


size = int(input())

board = [[x for x in input()] for _ in range(size)]

we_are_ready = False
removed_knights = 0

while True:
    check_hits()

    if we_are_ready:
        break

print(removed_knights)
