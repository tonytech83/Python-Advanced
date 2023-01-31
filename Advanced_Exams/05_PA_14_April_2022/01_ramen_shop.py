from collections import deque

# reads bowls as stack
bowls_of_ramen = [int(x) for x in input().split(', ')]
# reads customers in queue
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if ramen > customer:
        ramen -= customer
        bowls_of_ramen.append(ramen)
    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls_of_ramen))}')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f'Customers left: {", ".join(map(str, customers))}')
