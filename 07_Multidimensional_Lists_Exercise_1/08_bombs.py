def read_matrix():
    """
    This func read matrix from console with size.
    """
    size = int(input())
    return [[int(digit) for digit in input().split()] for _ in range(size)]


def check_coordinates(x, y):
    """
    This func returns only correct start and end row and column.
    """
    start_r, end_r = (x - 1, (x - 1) + 3)
    start_c, end_c = (y - 1, (y - 1) + 3)

    if x == 0:
        start_r, end_r = (x, x + 2)
    elif x == len(matrix) - 1:
        start_r, end_r = (x - 1, x + 1)

    if y == 0:
        start_c, end_c = (y, y + 2)
    elif y == len(matrix) - 1:
        start_c, end_c = (y - 1, y + 1)

    return start_r, end_r, start_c, end_c


matrix = read_matrix()
bombs_coordinates = input().split()

for bomb in bombs_coordinates:
    x, y = [int(x) for x in bomb.split(',')]
    bomb_power = matrix[x][y]

    if bomb_power <= 0:
        continue

    # takes the coordinates only in matrix size
    start_row, end_row, start_col, end_col = check_coordinates(x, y)

    # bomb explodes and deals damage equal to its integer value to all cells
    # around it (in every direction and in all diagonals)
    for row_idx in range(start_row, end_row):
        for col_dx in range(start_col, end_col):
            if matrix[row_idx][col_dx] > 0:
                matrix[row_idx][col_dx] -= bomb_power

alive_cells = 0
sum_of_cells = 0

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            sum_of_cells += num

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_cells}')
for row in matrix:
    print(*row, sep=' ')
