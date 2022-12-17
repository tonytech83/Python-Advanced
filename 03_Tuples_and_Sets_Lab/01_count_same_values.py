# take input in tuple
numbers = tuple(float(x) for x in input().split())

# crete dict to store uniq numbers
uniq_numbers = {}

# iterates trough numbers tuple and add uniq numbers in uniq_numbers dict
for num in numbers:
    if num not in uniq_numbers:
        uniq_numbers[num] = 0
    uniq_numbers[num] += 1

for number, count in uniq_numbers.items():
    print(f'{number:.1f} - {count} times')
