"""
exam: 03. Pets Hotel
judge: https://judge.softuni.org/Contests/Practice/Index/4089#2
"""


def accommodate_new_pets(capacity: int, max_weight: float, *args: tuple):
    hotel = {}
    result = ''

    for pet, weight in args:
        if capacity <= 0:
            result += 'You did not manage to accommodate all pets!\n'
            break

        if weight > max_weight:
            continue

        if pet not in hotel:
            hotel[pet] = 0

        hotel[pet] += 1
        capacity -= 1
    else:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'

    result += 'Accommodated pets:\n'

    for pet_type, count in sorted(hotel.items()):
        result += f'{pet_type}: {count}\n'

    return result


# Test input

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
