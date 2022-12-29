rows = int(input())

result = []
for _ in range(rows):
    result += [int(z) for z in input().split(', ')]

print(result)
