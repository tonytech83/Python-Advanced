from collections import deque

elfs_energy = deque(int(x) for x in input().split())
number_of_materials = [int(x) for x in input().split()]

energy_used = 0
toys_created = 0

turns_count = 0
while elfs_energy and number_of_materials:
    while elfs_energy and elfs_energy[0] < 5:
        elfs_energy.popleft()

    if not elfs_energy:
        break

    materials = number_of_materials.pop()
    energy = elfs_energy.popleft()

    turns_count += 1

    toys_to_be_created = 1
    spend_energy = materials
    energy_increase_with = 1

    if turns_count % 3 == 0:
        toys_to_be_created = 2
        spend_energy *= 2

    if turns_count % 5 == 0:
        toys_to_be_created = 0
        energy_increase_with = 0

    if energy >= spend_energy:
        toys_created += toys_to_be_created
        energy_used += spend_energy
        elfs_energy.append(energy - spend_energy + energy_increase_with)
    else:
        number_of_materials.append(materials)
        elfs_energy.append(energy * 2)

print(f'Toys: {toys_created}')
print(f'Energy: {energy_used}')

if elfs_energy:
    print(f'Elves left: {", ".join([str(x) for x in elfs_energy])}')
if number_of_materials:
    print(f'Boxes left: {", ".join([str(x) for x in number_of_materials])}')
