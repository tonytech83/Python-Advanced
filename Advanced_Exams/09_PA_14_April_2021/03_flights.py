# Exam: 03. Flights
# From: Python Advanced Exam - 23 October 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2828#2
from collections import deque


def flights(*args):
    data = deque(args)

    destinations = {}

    while data:
        flight = data.popleft()

        if flight == 'Finish':
            break

        passengers = data.popleft()

        if flight not in destinations:
            destinations[flight] = passengers
        else:
            destinations[flight] += passengers

    return destinations


# Test code 1
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# Test code 2
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

# Test code 3
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
