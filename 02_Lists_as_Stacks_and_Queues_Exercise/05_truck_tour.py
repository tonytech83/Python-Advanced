from collections import deque

petrol_pumps = int(input())

circle_road = deque()
visited_pump = 0

for _ in range(petrol_pumps):
    liters, distance = input().split()
    circle_road.append([int(liters), int(distance)])

for attempt in range(petrol_pumps):
    truck_tank = 0
    failed = False
    for petrol, next_pump_dist in circle_road:
        truck_tank += petrol - next_pump_dist

        if truck_tank < 0:
            failed = True
            break

    if failed:
        circle_road.append(circle_road.popleft())
    else:
        print(attempt)
        break
