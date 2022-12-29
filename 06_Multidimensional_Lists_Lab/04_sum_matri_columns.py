def read_matrix():
    return [[int(x) for x in input().split()] for _ in range(rows)]


rows, columns = [int(x) for x in input().split(', ')]
matrix = read_matrix()

columns_sums = []
for col_idx in range(columns):
    colum_sum = 0
    for row_idx in range(rows):
        colum_sum += matrix[row_idx][col_idx]
    columns_sums.append(colum_sum)

print(*columns_sums, sep='\n')
