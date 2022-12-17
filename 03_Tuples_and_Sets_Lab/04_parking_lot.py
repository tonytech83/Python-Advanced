n = int(input())

# create set where to store the car numbers
parking_lot = set()

# iterates in range of 'n'
for _ in range(n):
    # unpack input to direction and car_number
    direction, car_number = input().split(', ')
    # if direction is 'IN' adds car_number in parking_lot set
    if direction == 'IN':
        parking_lot.add(car_number)
    # if direction is 'OUT' removes car_number from parking_lot set
    else:
        parking_lot.remove(car_number)

# if parking_lot is not empty, prints car_numbers inside
if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')
