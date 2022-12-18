# the count of input lines
n = int(input())

# create set to store unique elements
unique_elements = set()

for _ in range(n):
    line = input().split()
    for element in line:
        unique_elements.add(element)

# prints elements in unique_elements set
[print(element) for element in unique_elements]
