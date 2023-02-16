# Exam: 03. List Pureness
# From: Python Advanced Exam - 24 October 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2551#2

import sys
from collections import deque


def best_list_pureness(lst, k):
    data = deque(lst)
    best_pureness = -sys.maxsize
    count_rotations = 0

    for rotation in range(k + 1):

        current_pureness = 0

        for idx, num in enumerate(data):
            current_pureness += idx * num

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            count_rotations = rotation

        data.appendleft(data.pop())

    return f'Best pureness {best_pureness} after {count_rotations} rotations'


# Test code 1
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

# Test code 2
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

# Test code 3
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
