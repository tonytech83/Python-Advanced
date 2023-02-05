# Exam: 02. North Pole Challenge
# From: Python Advanced Retake Exam - 15 December 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/3306#1

def read_matrix():
    """
    Reads matrix from console whit received rows and cols.
    Function returns matrix, position of cell marked with 'Y' and total items on matrix.
    """

    rows, cols = [int(x) for x in input().split(', ')]
    matrix = []
    position = []
    items = 0

    for row in range(rows):
        matrix.append(input().split())
        items += len([x for x in matrix[row] if x not in ['.', 'Y']])
        if 'Y' in matrix[row]:
            position.append(row)
            position.append(matrix[row].index('Y'))

    return matrix, position, items


def move_to_direction(position: list, current_command: str):
    """
    This func moves you regarding received direction and steps.
    If found any item manipulates collected_items dict and all_items
    """
    global workshop
    global collected_items
    global all_items

    row, col = position
    direction, steps = current_command.split('-')

    directions = {
        'right': (0, +1),
        'left': (0, -1),
        'up': (-1, 0),
        'down': (+1, 0)

    }

    for step in range(int(steps)):
        workshop[row][col] = 'x'

        row_ch, col_ch = directions[direction]
        row = row + row_ch
        if row > len(workshop) - 1 or row < -len(workshop) + 1:
            row = 0
        col = col + col_ch
        if col > len(workshop[0]) - 1 or col < -len(workshop[0]) + 1:
            col = 0

        if workshop[row][col] == DECORATIONS:
            collected_items['Christmas decorations'] += 1
            all_items -= 1
        elif workshop[row][col] == GIFTS:
            collected_items['Gifts'] += 1
            all_items -= 1
        elif workshop[row][col] == COOKIES:
            collected_items['Cookies'] += 1
            all_items -= 1

        workshop[row][col] = YOU

        if all_items == 0:
            break

    return [row, col]


workshop, your_position, all_items = read_matrix()
YOU = 'Y'
DECORATIONS = 'D'
GIFTS = 'G'
COOKIES = 'C'
END_COMMAND = 'End'
collected_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0
}

while True:
    command = input()
    if command == END_COMMAND:
        break

    your_position = move_to_direction(your_position, command)

    if all_items == 0:
        print('Merry Christmas!')
        break

print("You've collected:")
for item, count in collected_items.items():
    print(f'- {count} {item}')

[print(*row, sep=' ') for row in workshop]
