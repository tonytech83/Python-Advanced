from collections import deque

# read input for duration of green light and free window.
green_light = int(input())
free_window = int(input())

# create queue will store cars before receive 'green' input
waiting_cars = deque()
# store the car models and commands 'green' in queue received from input
crossroad = deque()
# boolean which help for final output
crash_happen = False
# keep the name of last popped car, this will help if there crash to print the car in final output
crashed_car = ''
# the variable will keep the last character on which crash is happen
hit = ''
# this variable will keep the count of cars which passed the crossroad
cars_passed = 0

while True:
    line = input()
    if line == 'END':
        break

    else:
        crossroad.append(line)

while crossroad:
    # popleft an element from crossroad queue and check if it is command 'green' or car name.
    # if the element is not 'green' add car in waiting_cars queue
    data = crossroad.popleft()

    if data != 'green':
        waiting_cars.append(data)

    # when we hit this else , this mean that we have a green light and cars from waiting_cars queue can start
    # entering in crossroad
    else:
        # check is there any cars in waiting_cars queue
        if not waiting_cars:
            break
        # popleft the name of the car
        current_car = waiting_cars.popleft()
        # keep the name of car if eventually we have a crash
        crashed_car = current_car

        # use local variable for green timer which we will reduce on each loop
        green_timer = green_light
        while True:
            for char in current_car:
                if green_timer == 0:
                    break
                green_timer -= 1
                # remove firs letter from name of the car
                current_car = current_car[1:]

            # if car name is empty string we considered that the car is passed the crossroad
            if not current_car:
                cars_passed += 1

            # if there is cars in waiting_cars queue and we still have flashed green light we are popping netx car
            # from waiting_cars queue
            if waiting_cars and green_timer > 0:
                current_car = waiting_cars.popleft()
            else:
                break

        # when we green light is off we should check is there car in crossroad
        if current_car:
            # use local variable for free window timer which we will reduce on each loop
            free_timer = free_window
            while len(current_car) != 0:
                for char in current_car:
                    if free_timer <= 0:
                        break
                    free_timer -= 1
                    # remove firs letter from name of the car
                    current_car = current_car[1:]
                # when the loop finished and we still have a letters in car name, this means that we have a crash
                if current_car:
                    # take the letter where the crash happens
                    hit = current_car[0]
                    crash_happen = True
                    break

                # if we don't have more letters in current_car, this means that car is passed successfully
                cars_passed += 1

if not crash_happen:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')
else:
    print('A crash happened!')
    print(f'{crashed_car} was hit at {hit[0]}.')
