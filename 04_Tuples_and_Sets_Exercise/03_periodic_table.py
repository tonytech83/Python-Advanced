# the count of input lines
n = int(input())

# create set to store unique elements
unique_elements = set()

for _ in range(n):
    current_set = set(input().split())
    unique_elements = unique_elements.union(current_set)

# prints elements in unique_elements set
[print(element) for element in unique_elements]
