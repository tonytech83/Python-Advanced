# Exam: 01. Pizza Orders
# From: Python Advanced Retake Exam - 14 April 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2828#0

from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
workers = [int(x) for x in input().split(', ')]
total_count = 0

while pizza_orders and workers:
    order = pizza_orders.popleft()

    if order > 10 or order <= 0:
        continue

    # if order <= 0:

    worker = workers.pop()

    if order > worker:
        order -= worker
        pizza_orders.appendleft(order)
        total_count += worker
    else:
        total_count += order

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_count}')
    print(f'Employees: {", ".join(str(x) for x in workers)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(x) for x in pizza_orders)}')
