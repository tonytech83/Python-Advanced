def read_race():
    """
    This func read race form console and returns it. Also take coordinates of tunnels as tuples and marks
    starting position of car with 'C'.
    """
    matrix = []
    tunnels = []

    for row in range(size):
        matrix.append(input().split())
        if 'T' in matrix[row]:
            tunnels.append((row, matrix[row].index('T')))

    matrix[0][0] = 'C'

    return matrix, tunnels


def move_car(coordinates: tuple, direction: str):
    """
    This func returns new coordinates of car relative to received direction.
    """
    global race

    r, c = coordinates
    race[r][c] = '.'

    directions = {
        'left': [r, c - 1],
        'right': [r, c + 1],
        'up': [r - 1, c],
        'down': [r + 1, c]
    }

    return directions[direction]


size = int(input())
racing_car = input()
race, tunnels = read_race()

covered_distance = 0
COMMAND_END = 'End'
FINAL = 'F'
TUNNEL = 'T'
CAR = 'C'
coordinates = (0, 0)
is_disqualified = False

while True:
    command = input()

    if command == COMMAND_END:
        is_disqualified = True
        break

    car_row, car_col = move_car(coordinates, command)
    covered_distance += 10

    if race[car_row][car_col] == FINAL:
        race[car_row][car_col] = CAR
        break

    elif race[car_row][car_col] == TUNNEL:
        race[car_row][car_col] = '.'
        for tunel_coordinates in tunnels:
            if tunel_coordinates != (car_row, car_col):
                coordinates = tunel_coordinates
        covered_distance += 20
        continue

    race[car_row][car_col] = CAR
    coordinates = (car_row, car_col)

if not is_disqualified:
    print(f'Racing car {racing_car} finished the stage!')
else:
    print(f'Racing car {racing_car} DNF.')

print(f'Distance covered {covered_distance} km.')
[print(*row, sep='') for row in race]
