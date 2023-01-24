gifts = int(input())
size = int(input())

neighborhood = []
santa_row = 0
santa_col = 0
count_nice_kids = 0
gifts_given = 0

# read neighborhood from console and collect santa coordinates and count nice kids
for row in range(size):
    row_elements = input().split()
    count_nice_kids += row_elements.count('V')
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row = row
            santa_col = col
    neighborhood.append(row_elements)

while gifts > 0:
    command = input()

    if command == 'Christmas morning':
        break

    directions = {
        'left': lambda r, c: (r, c - 1),
        'up': lambda r, c: (r - 1, c),
        'right': lambda r, c: (r, c + 1),
        'down': lambda r, c: (r + 1, c),
    }

    # takes new position of santa and mark old with '-'
    next_row, next_col = directions[command](santa_row, santa_col)
    neighborhood[santa_row][santa_col] = '-'

    # if the new position is nice kid
    if neighborhood[next_row][next_col] == 'V':
        count_nice_kids -= 1
        gifts -= 1
        gifts_given += 1
        santa_row, santa_col = next_row, next_col

    # if the new position is cookie
    elif neighborhood[next_row][next_col] == 'C':
        for direction in directions:
            row_idx, col_idx = directions[direction](next_row, next_col)
            if neighborhood[row_idx][col_idx] == 'V':
                count_nice_kids -= 1
                gifts -= 1
                gifts_given += 1
            elif neighborhood[row_idx][col_idx] == 'X':
                gifts -= 1
            neighborhood[row_idx][col_idx] = '-'
    # if the new position is '-' or naughty kid
    else:
        santa_row, santa_col = next_row, next_col

    # mark new position of santa with 'S'
    neighborhood[next_row][next_col] = 'S'

if gifts <= 0 < count_nice_kids:
    print('Santa ran out of presents!')

[print(*row, sep=' ') for row in neighborhood]

if count_nice_kids == 0:
    print(f'Good job, Santa! {gifts_given} happy nice kid/s.')
else:
    print(f'No presents for {count_nice_kids} nice kid/s.')
