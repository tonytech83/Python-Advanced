def read_chessboard():
    """
    Reads chessboard from console and returns matrix, white pawn coordinates and black pawn coordinates.
    """
    matrix = []
    white_position = []
    black_position = []
    for row in range(8):
        matrix.append(input().split())
        if 'w' in matrix[row]:
            white_position.append(row)
            white_position.append(matrix[row].index('w'))

        if 'b' in matrix[row]:
            black_position.append(row)
            black_position.append(matrix[row].index('b'))

    return matrix, white_position, black_position


def check_for_capture(coordinates, pawn_color):
    """
    This func checks if the pawn can attack other pawn. Using try-except to if new coordinates are outside of board.
    If attack is possible manipulates chessboard and coordinates of current pawn.
    """
    global chessboard
    global white
    global black

    # current coordinates of pawn
    row, col = coordinates

    # possible moves for withe pawn.
    white_directions = {
        'up_left': (row - 1, col - 1),
        'up_right': (row - 1, col + 1),
    }

    if pawn_color == WHITE_PAWN:
        for direction in white_directions:
            move_row, move_col = white_directions[direction]
            try:
                if chessboard[move_row][move_col] == BLACK_PAWN:
                    chessboard[row][col] = EMPTY_POSITION
                    chessboard[move_row][move_col] = WHITE_PAWN
                    white = move_row, move_col
                    return True
            except IndexError:
                continue

    # possible moves for black pawn
    black_directions = {
        'down_left': (row + 1, col - 1),
        'down_right': (row + 1, col + 1)
    }

    if pawn_color == BLACK_PAWN:
        for direction in black_directions:
            move_row, move_col = black_directions[direction]
            try:
                if chessboard[move_row][move_col] == WHITE_PAWN:
                    chessboard[row][col] = EMPTY_POSITION
                    chessboard[move_row][move_col] = BLACK_PAWN
                    black = move_row, move_col
                    return True
            except IndexError:
                continue

    return False


def pawn_move(coordinates, pawn_color):
    """
    This func moves pawn forward. Also:
    - manipulates boolean queen if pawn reach the end of board
    - manipulates boolean capture if attack is possible
    - manipulates white/black coordinates if attack is not possible
    """
    global chessboard
    global capture
    global queen
    global white
    global black

    if pawn_color == WHITE_PAWN:
        if check_for_capture(coordinates, pawn_color):
            capture = True
        else:
            chessboard[white[0]][white[1]] = EMPTY_POSITION
            if white[0] - 1 < 0:
                queen = True
            else:
                chessboard[white[0] - 1][white[1]] = WHITE_PAWN
                white = white[0] - 1, white[1]

    if pawn_color == BLACK_PAWN:
        if check_for_capture(coordinates, pawn_color):
            capture = True
        else:
            chessboard[black[0]][black[1]] = EMPTY_POSITION

            if black[0] + 1 > 7:
                queen = True
            else:
                chessboard[black[0] + 1][black[1]] = BLACK_PAWN
                black = black[0] + 1, black[1]


chessboard, white, black = read_chessboard()

capture = False
queen = False
WHITE_PAWN = 'w'
BLACK_PAWN = 'b'
EMPTY_POSITION = '-'
winner = ''

pawn_color = WHITE_PAWN
coordinates_on_turn = white
while not capture:
    pawn_move(coordinates_on_turn, pawn_color)

    if capture:
        if pawn_color == WHITE_PAWN:
            coordinates_on_turn = white
            winner = 'White'
        else:
            winner = 'Black'
            coordinates_on_turn = black
        break

    if queen:
        if pawn_color == WHITE_PAWN:
            coordinates_on_turn = white
            winner = 'White'
        else:
            winner = 'Black'
            coordinates_on_turn = black
        break

    if pawn_color == BLACK_PAWN:
        coordinates_on_turn = white
        pawn_color = WHITE_PAWN
    else:
        coordinates_on_turn = black
        pawn_color = BLACK_PAWN

column_to_letter = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

row_to_string = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}

if capture:
    print(
        f'Game over! {winner} win, capture on'
        f' {column_to_letter[coordinates_on_turn[1]]}{row_to_string[coordinates_on_turn[0]]}.'
    )
else:
    print(
        f'Game over! {winner} pawn is promoted to a queen at'
        f' {column_to_letter[coordinates_on_turn[1]]}{row_to_string[coordinates_on_turn[0]]}.'
    )
