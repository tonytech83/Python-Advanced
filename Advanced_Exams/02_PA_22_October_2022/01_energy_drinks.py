from collections import deque

TOTAL_CAFFEINE_PER_DAY = 300

# stack of caffeine
milligrams_of_caffeine = [int(x) for x in input().split(', ')]
# queue of drinks
energy_drinks = deque(int(x) for x in input().split(', '))

caffeine_drank = 0

while True:
    current_caffeine = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()
    drink_caffeine = current_caffeine * current_drink

    if caffeine_drank + drink_caffeine <= TOTAL_CAFFEINE_PER_DAY:
        caffeine_drank += drink_caffeine
    else:
        energy_drinks.append(current_drink)
        caffeine_drank -= 30 if caffeine_drank >= 30 else 0

    if not milligrams_of_caffeine or not energy_drinks:
        break

if energy_drinks:
    print(f'Drinks left: {", ".join([str(s) for s in energy_drinks])}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {caffeine_drank} mg caffeine.')
