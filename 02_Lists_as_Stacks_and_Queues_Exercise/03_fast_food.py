from collections import deque

# quantity of the food for the day
food_quantity = int(input())

# sequence of integers (separated by a single space), each representing the quantity of food in each order
orders_queue = deque(int(x) for x in input().split())

# print the quantity of the biggest order
print(max(orders_queue))

# loop until we have orders in orders_queue and food_quantity >= 0
while orders_queue:
    current_order = orders_queue.popleft()
    if food_quantity - current_order >= 0:
        food_quantity -= current_order
    else:
        orders_queue.appendleft(current_order)
        print(f'Orders left: {" ".join(str(x) for x in orders_queue)}')
        break

if not orders_queue:
    print('Orders complete')
