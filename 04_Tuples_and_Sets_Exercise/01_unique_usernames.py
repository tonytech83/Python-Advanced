n = int(input())

# reads input from console n-times and adds to set. This will ensure that we only record the unique names.
unique_names = set(input() for x in range(n))

# prints all stored names in unique_names set
[print(name) for name in unique_names]
