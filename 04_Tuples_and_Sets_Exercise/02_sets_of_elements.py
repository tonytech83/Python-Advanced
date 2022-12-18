# reads 'n' and 'm' as integers
n, m = [int(x) for x in input().split()]

# reads 'n' times elements from console and store them in set
first_set = {int(input()) for x in range(n)}

# reads 'm' times elements from console and store them in set
second_set = {int(input()) for x in range(m)}

# find same elements between two sets
same_elements = first_set.intersection(second_set)
for number in same_elements:
    print(number)
