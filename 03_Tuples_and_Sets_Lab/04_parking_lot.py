def output():
    if parking_lot:
        [print(car_plate) for car_plate in parking_lot]
    else:
        print('Parking Lot is Empty')


n = int(input())

# create set where to store the car numbers
parking_lot = set()
DIRECTION_IN = 'IN'
DIRECTION_OUT = 'OUT'

# iterates in range of 'n'
for _ in range(n):
    # unpack input to direction and car_number
    direction, car_number = input().split(', ')

    # if direction is 'IN' adds car_number in parking_lot set
    if direction == DIRECTION_IN:
        parking_lot.add(car_number)

    # if direction is 'OUT' removes car_number from parking_lot set
    elif direction == DIRECTION_OUT:
        parking_lot.remove(car_number)

output()
