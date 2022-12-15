from collections import deque

cups = deque([int(x) for x in input().split()])  # from left to right
bottles = deque([int(x) for x in input().split()])  # from right to left

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()

    while current_cup > 0:
        current_bottle = bottles.pop()
        current_cup -= current_bottle
        if current_cup >= 0:
            continue
        else:
            wasted_water += abs(current_cup)

        if not bottles:
            break

if not cups:
    print(f'Bottles: {" ".join(str(x) for x in bottles)}')
else:
    print(f'Cups: {" ".join(str(x) for x in cups)}')

print(f'Wasted litters of water: {wasted_water}')
