from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

healing_items = {
    30: ['Patch', 0],
    40: ['Bandage', 0],
    100: ['MedKit', 0],
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    healing_mix = textile + medicament

    if healing_mix in healing_items:
        healing_items[healing_mix][1] += 1
    elif healing_mix > 100:
        healing_items[100][1] += 1
        medicaments.append(medicaments.pop() + healing_mix - 100)
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
else:
    if not textiles:
        print('Textiles are empty.')
    if not medicaments:
        print('Medicaments are empty.')

for name, quantity in sorted(healing_items.values(), key=lambda kvp: (-kvp[1], kvp[0])):
    if quantity > 0:
        print(f'{name} - {quantity}')

if medicaments:
    print(f'Medicaments left: {", ".join(map(str, reversed(medicaments)))}')
if textiles:
    print(f'Textiles left: {", ".join(map(str, textiles))}')
