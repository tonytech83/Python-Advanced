# Exam: 01. Matching
# From: Python Advanced Retake Exam - 16 December 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2720#0

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    current_female = females.popleft()
    current_male = males.pop()

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        males.append(current_male)
        females.popleft()
        continue

    if current_male % 25 == 0:
        females.appendleft(current_female)
        males.pop()
        continue

    if current_female != current_male:
        males.append(current_male - 2)
        continue

    matches += 1

print(f'Matches: {matches}')
print(f'Males left: {", ".join(map(str, reversed(males))) if males else "none"}')
print(f'Females left: {", ".join(map(str, females)) if females else "none"}')
