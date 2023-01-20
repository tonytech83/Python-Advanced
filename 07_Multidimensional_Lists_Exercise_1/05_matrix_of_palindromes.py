# read rows and columns to generate the matrix of palindromes of 3 letters.
rows, columns = [int(x) for x in input().split()]

START = ord('a')

# rows define the first and the last letter
# columns + rows define the middle letter
for row in range(START, START + rows):
    for col in range(columns):
        palindrom = f'{chr(row)}{chr(col + row)}{chr(row)}'
        print(palindrom, end=' ')

    print()
