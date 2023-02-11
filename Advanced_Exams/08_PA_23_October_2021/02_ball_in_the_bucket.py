# Exam: 02. Ball in the Bucket
# From: Python Advanced Exam - 23 October 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/3227#1
import sys
from collections import deque


def create_playground():
    """
    This func creates playground and collect coordinates of all buckets inside playground.
    """
    matrix = []
    buckets_coordinates = []

    for row in range(size):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
        for idx in range(len(matrix[row])):
            if matrix[row][idx] == 'B':
                buckets_coordinates.append((row, idx))

    return matrix, buckets_coordinates


def calculate_points(current_throw: tuple, playground: list):
    """
    This func sum all numbers in column for current throw and increases the value of total scored points with this sum.
    """
    global scored_points

    col = current_throw[1]

    current_col_points = 0
    for idx in range(size):
        current_col_points += playground[idx][col] if isinstance(playground[idx][col], int) else 0

    scored_points += current_col_points


def output():
    """
    Prints the regarding scored points.
    """
    if scored_points < 100:
        print(f'Sorry! You need {abs(100 - scored_points)} points more to win a prize.')

    prizes_collection = {
        'Football': range(100, 200),
        'Teddy Bear': range(200, 300),
        'Lego Construction Set': range(300, sys.maxsize)
    }

    for prize, points in prizes_collection.items():
        if scored_points in points:
            print(f"Good job! You scored {scored_points} points, and you've won {prize}.")


def main():
    """
    Main func which is reads the player trows, iterates through them if the throw is inside buckets list call
    func calculate_points. At the end call output func.
    """
    playground, buckets = create_playground()

    throw_one = tuple(int(x) for x in input().strip('()').split(', '))
    throw_two = tuple(int(x) for x in input().strip('()').split(', '))
    throw_three = tuple(int(x) for x in input().strip('()').split(', '))

    throws = deque([throw_one, throw_two, throw_three])

    for throw in throws:
        if throw in buckets:
            calculate_points(throw, playground)
            buckets.remove(throw)

    output()


size = 6
scored_points = 0

main()
