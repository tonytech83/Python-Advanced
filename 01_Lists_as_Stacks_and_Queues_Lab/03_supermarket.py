from collections import deque

customers = deque()
COMMAND_END = 'END'
COMMAND_PAID = 'Paid'

while True:
    customer_name = input()

    if customer_name == COMMAND_END:
        print(f'{len(customers)} people remaining.')
        break

    if customer_name == COMMAND_PAID:
        while customers:
            print(customers.popleft())
        continue

    customers.append(customer_name)
