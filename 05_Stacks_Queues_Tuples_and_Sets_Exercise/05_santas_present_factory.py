from collections import deque


def presents_pair():
    """
    This function checks if manage to craft either one of the pairs:
    - a doll and a train
    - a teddy bear and a bicycle
    :returns: message
    """
    if {'Doll', 'Wooden train'}.issubset(crafted_toys) or {'Teddy bear', 'Bicycle'}.issubset(crafted_toys):
        return 'The presents are crafted! Merry Christmas!'
    return 'No presents this Christmas!'


# read materials from console input in stack
material_boxes = [int(x) for x in input().split()]

# read magic from console input in queue
magic_values = deque(int(x) for x in input().split())

presents_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

# create dict where to store crafted toys and count of each toy
crafted_toys = {}

# Stop crafting presents when run out of boxes of materials or magic level values.
while material_boxes and magic_values:
    material = material_boxes.pop()
    magic = magic_values.popleft()

    # If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
    if magic == 0 and material == 0:
        continue
    if magic == 0:
        material_boxes.append(material)
        continue
    if material == 0:
        magic_values.appendleft(magic)
        continue

    # calculates total magic level
    magic_level = material * magic

    # if magic level is in presents_table dict values craft toy and add to crafted toys dict
    if magic_level in presents_table:
        crafted_toy = presents_table[magic_level]
        if crafted_toy not in crafted_toys:
            crafted_toys[crafted_toy] = 1
        else:
            crafted_toys[crafted_toy] += 1
        continue

    # If the product of the operation is a negative number, you should sum the values together,
    # remove them both from their positions, and add the result to the materials.
    if magic_level < 0:
        material_boxes.append(material + magic)
    # If the product doesn't equal one of the magic levels in the table and is a positive number,
    # remove only the magic value and increase the material value by 15.
    else:
        material_boxes.append(material + 15)

# On the first line - print whether you've succeeded in crafting the presents:
print(presents_pair())

# On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
if material_boxes:
    print(f'Materials left: {", ".join(map(str, reversed(material_boxes)))}')
if magic_values:
    print(f'Magic left: {", ".join(map(str, magic_values))}')

# On the next lines print the presents you have crafted, ordered alphabetically
[print(f'{toy}: {count}') for toy, count in sorted(crafted_toys.items())]
