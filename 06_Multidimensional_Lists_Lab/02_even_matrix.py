rows = int(input())

# list of lists comprehension - 2 dimensional matrix
matrix = [[s for s in [int(x) for x in input().split(', ')] if int(s) % 2 == 0] for row in range(rows)]

print(matrix)
