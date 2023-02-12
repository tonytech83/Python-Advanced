# Exam: 01. Fireworks Show
# From: Python Advanced Exam - 14 February 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2812#0
from collections import deque

firework_types = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]

while firework_effects and explosive_power:
    effect = firework_effects.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
        continue
    if power <= 0:
        firework_effects.appendleft(effect)
        continue

    mix_sum = effect + power

    if mix_sum % 3 == 0 and mix_sum % 5 != 0:
        firework_types['Palm Fireworks'] += 1
    elif mix_sum % 5 == 0 and mix_sum % 3 != 0:
        firework_types['Willow Fireworks'] += 1
    elif mix_sum % 5 == 0 and mix_sum % 3 == 0:
        firework_types['Crossette Fireworks'] += 1
    else:
        explosive_power.append(power)
        firework_effects.append(effect - 1)

    # breaks when have 3 of each of the firework types
    if all(True if value >= 3 else False for value in firework_types.values()):
        print('Congrats! You made the perfect firework show!')
        break

else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join(str(x) for x in firework_effects)}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_power)}')

[print(f'{firework}: {count}') for firework, count in firework_types.items()]
