from collections import deque

customers = deque()

while True:
    customer_name = input()

    if customer_name == 'End':
        print(f'{len(customers)} people remaining.')
        break

    if customer_name == 'Paid':
        while customers:
            print(customers.popleft())
        continue

    customers.append(customer_name)
