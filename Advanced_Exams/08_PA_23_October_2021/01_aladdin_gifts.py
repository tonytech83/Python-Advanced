# Exam: 01. Aladdin's Gifts
# From: Python Advanced Exam - 23 October 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/3227#0

from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
crafted_gifts = {}


def crafting():
    """
    This func sum material and magic and checks is the sum is in ranges of dict with wedding present.
    """
    global materials
    global magic_levels
    global crafted_gifts

    wedding_present = {
        'Gemstone': range(100, 200),
        'Porcelain Sculpture': range(200, 300),
        'Gold': range(300, 400),
        'Diamond Jewellery': range(400, 500)
    }

    while materials and magic_levels:
        current_material = materials.pop()
        current_magic = magic_levels.popleft()

        mix_result = current_material + current_magic

        if mix_result < 100:
            if mix_result % 2 == 0:
                mix_result = 2 * current_material + 3 * current_magic
            else:
                mix_result *= 2

        elif mix_result > 499:
            mix_result //= 2

        for gift, magic_range in wedding_present.items():
            if mix_result in magic_range:
                if gift not in crafted_gifts:
                    crafted_gifts[gift] = 1
                else:
                    crafted_gifts[gift] += 1

    output()


def output():
    """
    This function prints the requested output regarding exam requirements.
    """
    if ('Gemstone' in crafted_gifts and 'Porcelain Sculpture' in crafted_gifts) or \
            ('Gold' in crafted_gifts and 'Diamond Jewellery' in crafted_gifts):
        print('The wedding presents are made!')
    else:
        print('Aladdin does not have enough wedding presents.')

    if materials:
        print(f'Materials left: {", ".join(str(x) for x in materials)}')
    if magic_levels:
        print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

    for gift, quantity in sorted(crafted_gifts.items()):
        print(f'{gift}: {quantity}')


crafting()
