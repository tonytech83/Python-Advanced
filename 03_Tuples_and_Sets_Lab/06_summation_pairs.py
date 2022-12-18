"""
On the first line, you will receive a string of numbers separated by space. On the second line,
you'll receive a target number. Your task is to find all pairs of numbers whose sum equals the target number.
For each found pair print "{number} + {number} = {target_number}".
Then, save only the unique pairs. Note: (1, 2) and (2, 1) are unique.
Also, you should keep track of how many iterations you've done.
At the end print all the iterations done in format: "Iterations done: {total_number_of_iterations}".
On the following lines, print the unique pairs in the format: "(first_number, second_number)".
The order in which we print the result does not matter.

Example:
Input
1 5 4 2 2 3 1 3 2
4

Output
1 + 3 = 4
1 + 3 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
3 + 1 = 4
1 + 3 = 4
Iterations done: 36
(3, 1)
(1, 3)
(2, 2)
"""

numbers = [int(x) for x in input().split()]
target = int(input())

iterations = 0
unique_pairs = set()

for idx1 in range(len(numbers)):
    for idx2 in range(idx1 + 1, len(numbers)):
        iterations += 1
        p1 = numbers[idx1]
        p2 = numbers[idx2]
        if p1 + p2 == target:
            print(f'{p1} + {p2} = {target}')
            unique_pairs.add(f'{p1} + {p2}')

print(f'Iterations done: {iterations}')
[print(f'({x})') for x in unique_pairs]
