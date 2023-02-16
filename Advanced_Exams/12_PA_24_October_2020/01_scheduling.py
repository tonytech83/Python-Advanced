# Exam: 01. Scheduling
# From: Python Advanced Exam - 24 October 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2551#0

import sys

jobs = [int(x) for x in input().split(', ')]
the_job_idx = int(input())

clock_cycles = 0
max_value = sys.maxsize

while True:
    current_job_idx = jobs.index(min(jobs))
    current_job = jobs[current_job_idx]

    if the_job_idx == current_job_idx:
        clock_cycles += jobs[current_job_idx]
        break

    clock_cycles += current_job
    jobs[current_job_idx] = max_value

print(clock_cycles)
