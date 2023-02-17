# Exam: 01. Taxi Express
# From: Python Advanced Retake Exam - 19 August 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2463#0

from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]

total_time = sum(customers)

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_customer > current_taxi:
        customers.appendleft(current_customer)

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str, customers))}')
