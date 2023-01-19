n = int(input())

# reads input from console n-times and adds them to set.
# using set will ensure that we only record the unique names.
unique_names = set(input() for _ in range(n))

# prints all stored names in unique_names set
[print(name) for name in unique_names]

## One line solution
# print(*{input() for _ in range(int(input()))}, sep='\n')
