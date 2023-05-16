class Player:
    def __init__(self, name: str, is_resting: bool):
        self.name = name
        self.is_resting = is_resting

    def wake(self):
        self.is_resting = False

    def rest(self):
        self.is_resting = True


def read_maze():
    """
    Reads matrix from console
    """
    new_maze = []
    for row in range(MAZE_SIZE):
        new_maze.append(input().split())

    return new_maze


MAZE_SIZE = 6
EXIT, TRAP, WALL, EMPTY = 'E', 'T', 'W', '.'
player_names = input().split(', ')
maze = read_maze()

current_player = Player(player_names[0], False)
next_player = Player(player_names[1], False)

while True:

    row, col = [int(x) for x in input() if x.isdigit()]

    if current_player.is_resting:
        current_player.wake()
        current_player, next_player = next_player, current_player
        continue

    if maze[row][col] == EXIT:
        print(f"{current_player.name} found the Exit and wins the game!")
        break

    elif maze[row][col] == TRAP:
        print(f"{current_player.name} is out of the game! The winner is {next_player.name}.")
        break

    elif maze[row][col] == WALL:
        print(f"{current_player.name} hits a wall and needs to rest.")
        current_player.rest()

    current_player, next_player = next_player, current_player
