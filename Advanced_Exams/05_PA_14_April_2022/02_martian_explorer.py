def land_reader():
    """
    Reads Mars land from console and searches for rover marked with 'E'. Returns the land and rovers coordinates.
    """
    land = []
    rover_row = 0
    rover_col = 0
    for row in range(6):
        land.append(input().split())
        if ROVER in land[row]:
            rover_row = row
            rover_col = land[row].index(ROVER)

    return land, rover_row, rover_col


def check_new_position(row, col):
    """
    This func received the next move of rover. If the rover goes out of the field, it should continue from the opposite
    side in the same direction.
    """
    if row in range(6) and col in range(6):
        return row, col

    row = 0 if row > 5 else row
    row = 5 if row < 0 else row
    col = 0 if col > 5 else col
    col = 5 if col < 0 else col

    return row, col


def rover_move(direction, coordinates):
    """
    This func calculates the new position in the land. Relative to new position prints a message and finally returns
    position of the rover.
    """
    global found_deposits
    global deposit_types
    global is_broken

    r, c = coordinates
    directions = {
        'left': [r, c - 1],
        'right': [r, c + 1],
        'up': [r - 1, c],
        'down': [r + 1, c]
    }

    next_row, next_col = directions[direction]

    rover_row, cover_col = check_new_position(next_row, next_col)

    if mars_land[rover_row][cover_col] in deposit_types:
        found_deposits.add(deposit_types[mars_land[rover_row][cover_col]])
        print(f'{deposit_types[mars_land[rover_row][cover_col]]} deposit found at ({rover_row}, {cover_col})')

    if mars_land[rover_row][cover_col] == ROCK:
        print(f'Rover got broken at ({rover_row}, {cover_col})')
        is_broken = True

    return rover_row, cover_col


deposit_types = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete'
}

ROVER = 'E'
ROCK = 'R'
is_broken = False
is_suitable_area = False

mars_land, *rover_coordinates = land_reader()
found_deposits = set()
commands = input().split(', ')

for command in commands:
    rover_coordinates = rover_move(command, rover_coordinates)

    if len(found_deposits) == 3:
        is_suitable_area = True

    if is_broken:
        break

if is_suitable_area:
    print('Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
