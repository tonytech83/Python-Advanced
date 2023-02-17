# Exam: 01. Bombs
# From: Python Advanced Exam - 27 June 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2456#0

from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

bomb_types = {
    60: ['Cherry Bombs', 0],
    40: ['Datura Bombs', 0],
    120: ['Smoke Decoy Bombs', 0],
}

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    mix = effect + casing

    if mix in bomb_types:
        bomb_types[mix][1] += 1
    else:
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing - 5)

    if all([True if value[1] >= 3 else False for value in bomb_types.values()]):
        print('Bene! You have successfully filled the bomb pouch!')
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f'Bomb Effects: {", ".join(map(str, bomb_effects)) if bomb_effects else "empty"}')
print(f'Bomb Casings: {", ".join(map(str, bomb_casings)) if bomb_casings else "empty"}')
print('\n'.join(f'{name}: {quantity}' for name, quantity in bomb_types.values()))
