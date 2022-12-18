from collections import deque

# read input for duration of green light and free window.
green_light = int(input())
free_window = int(input())

# create queue will store cars before receive 'green' input
waiting_cars = deque()

# boolean which help for final output
crash_happen = False

cars_passed = 0
crashed_car = ''
hit = ''

while not crash_happen:
    line = input()
    if line == 'END':
        break

    if line == 'green':
        current_green = green_light
        while waiting_cars and current_green > 0:
            current_car = waiting_cars.popleft()
            if current_green + free_window >= len(current_car):
                cars_passed += 1
            else:
                crash_happen = True
                crashed_car = current_car
                hit = current_car[current_green + free_window]
                break
            current_green -= len(current_car)
    else:
        waiting_cars.append(line)

if not crash_happen:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')
else:
    print('A crash happened!')
    print(f'{crashed_car} was hit at {hit}.')
