matrix = [[y for y in x.strip().split()] for x in input().split('|')]

result = []

while matrix:
    row = matrix.pop()
    result += row

print(*result)
