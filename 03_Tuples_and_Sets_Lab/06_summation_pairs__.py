from itertools import combinations

numbers = [int(x) for x in input().split()]
target = int(input())

iterations = 0
unique_pairs = set()

# creates uniques combinations of two elements from all elements in numbers list
# unpack the tuple to first_num and second_name
for first_num, second_num in combinations(numbers, 2):
    iterations += 1
    if first_num + second_num == target:
        unique_pairs.add((first_num, second_num))
        print(f'{first_num} + {second_num} = {target}')

print(f'Iterations done: {iterations}')
[print(f'({x})') for x in unique_pairs]
