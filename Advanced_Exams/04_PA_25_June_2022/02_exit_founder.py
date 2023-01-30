def read_maze():
    """
    Reads matrix from console
    """
    new_maze = []
    for row in range(MAZE_SIZE):
        new_maze.append(input().split())

    return new_maze


def player_move(coordinates, player):
    """
    Moves player to received coordinates and change some of global boolean relative to the visited cell in maze.
    """
    global found_exit
    global player_one_rest
    global player_two_rest
    global fall_in_trap

    row, col = [int(x) for x in coordinates if x.isdigit()]

    if maze[row][col] == EXIT:
        found_exit = True

    elif maze[row][col] == TRAP:
        fall_in_trap = True

    elif maze[row][col] == WALL:
        if player == player_one:
            player_one_rest = True
        else:
            player_two_rest = True


player_one, player_two = input().split(', ')
MAZE_SIZE = 6
EXIT = 'E'
TRAP = 'T'
WALL = 'W'
maze = read_maze()

player_turn = 0
player_one_rest = False
player_two_rest = False
found_exit = False
fall_in_trap = False

while True:

    turn_coordinates = input()
    player_turn += 1

    if player_turn % 2 == 1:
        player = player_one
        if player_one_rest:
            player_one_rest = False
            continue
    else:
        player = player_two
        if player_two_rest:
            player_two_rest = False
            continue

    player_move(turn_coordinates, player)

    if found_exit:
        print(f'{player} found the Exit and wins the game!')
        break

    if player_one_rest and player == player_one:
        print(f'{player} hits a wall and needs to rest.')
    elif player_two_rest and player == player_two:
        print(f'{player} hits a wall and needs to rest.')

    if fall_in_trap:
        print(f'{player} is out of the game! The winner is {player_two if player == player_one else player_one}.')
        break
