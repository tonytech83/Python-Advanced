n = int(input())

odd_sums = set()
even_sums = set()

# sum the ASCII values of each letter in the name and
# integer divide it by the number of the current row (starting from 1)
for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row

    if name_sum % 2 == 0:
        even_sums.add(name_sum)
    else:
        odd_sums.add(name_sum)

# If the sums of the two sets are equal, print the union of the values, separated by ", ".
if sum(odd_sums) == sum(even_sums):
    print(*(odd_sums.union(even_sums)), sep=', ')

# If the sum of the odd numbers is bigger than the sum of the even numbers,
# print the different values, separated by ", ".
elif sum(odd_sums) > sum(even_sums):
    print(*(odd_sums.difference(even_sums)), sep=', ')

# If the sum of the even numbers is bigger than the sum of the odd numbers,
# print the symmetric-different values, separated by ", ".
else:
    print(*(odd_sums.symmetric_difference(even_sums)), sep=', ')
