n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')

    # split both ranges and received start and end numbers
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    # generates sets from range
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    # intersect both sets
    current_intersection = first_set.intersection(second_set)

    # compare length of current_intersection and longest_intersection
    # if current_intersection is bigger longest_intersection rewrites longest_intersection with current_intersection
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
