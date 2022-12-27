from collections import deque

# read bees values from console input in queue
bees_values = deque(int(x) for x in input().split())

# read nectar values from console in stack
nectar_values = [int(x) for x in input().split()]

# read symbols in queue
symbols = deque(x for x in input().split())

# create dict with all possible calculations
operations = {
    '+': lambda a, b: abs(a + b),
    '-': lambda a, b: abs(a - b),
    '*': lambda a, b: abs(a * b),
    '/': lambda a, b: abs(a / b),
}

honey_made = 0

while bees_values and nectar_values:

    current_bee = bees_values.popleft()
    current_nectar = nectar_values.pop()

    if current_nectar >= current_bee:
        if current_nectar == 0:
            continue
        current_symbol = symbols.popleft()
        honey_made += operations[current_symbol](current_bee, current_nectar)
    else:
        bees_values.appendleft(current_bee)

print(f'Total honey made: {honey_made}')
if bees_values:
    print(f'Bees left: {", ".join(map(str, bees_values))}')
if nectar_values:
    print(f'Nectar left: {", ".join(map(str, nectar_values))}')
