"""
exam: 01. Rubber Duck Debuggers
url: https://judge.softuni.org/Contests/Practice/Index/3893#0
"""
from collections import deque

tasks_time = deque(int(x) for x in input().split())
tasks_number = [int(x) for x in input().split()]

rubber_ducks = {
    "Darth Vader Ducky": [range(61), 0],
    "Thor Ducky": [range(61, 121), 0],
    "Big Blue Rubber Ducky": [range(121, 181), 0],
    "Small Yellow Rubber Ducky": [range(181, 241), 0],
}

while tasks_time and tasks_number:
    task_time = tasks_time.popleft()
    task_number = tasks_number.pop()

    calculated_time = task_number * task_time

    if calculated_time > 240:
        task_number -= 2
        tasks_time.append(task_time)
        tasks_number.append(task_number)
        continue

    for time_range in rubber_ducks:
        if calculated_time in rubber_ducks[time_range][0]:
            rubber_ducks[time_range][1] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{duck}: {rubber_ducks[duck][1]}") for duck in rubber_ducks]
