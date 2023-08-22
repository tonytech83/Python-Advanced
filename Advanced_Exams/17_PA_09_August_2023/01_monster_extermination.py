"""
exam: 01. Monster Extermination
judge: https://judge.softuni.org/Contests/Practice/Index/4089#0
"""
from collections import deque

monsters_armor = deque(int(x) for x in input().split(','))
solder_strikes = [int(x) for x in input().split(',')]
defeated_monsters = 0

while monsters_armor and solder_strikes:
    armor = monsters_armor.popleft()
    strike = solder_strikes.pop()

    if strike >= armor:
        strike -= armor
        defeated_monsters += 1

        if solder_strikes:
            solder_strikes[-1] += strike
        elif not solder_strikes and strike > 0:
            solder_strikes.append(strike)
    else:
        armor -= strike
        monsters_armor.append(armor)

if not monsters_armor:
    print('All monsters have been killed!')

if not solder_strikes:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {defeated_monsters}')
