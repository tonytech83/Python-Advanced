n = int(input())

# create set where to store only unique names
names_set = set()

# read input in range of 'n' and add input to names_set
[names_set.add(input()) for name in range(n)]

# print all names stored in names_set
[print(name) for name in names_set]
