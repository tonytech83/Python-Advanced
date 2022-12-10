from collections import deque

dispenser = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    if command == 'End':
        print(f'{dispenser} liters left')
        break

    if command.isdigit():

        liters = int(command)
        person = people.popleft()

        if dispenser >= liters:
            print(f'{person} got water')
            dispenser -= liters
        else:
            print(f'{person} must wait')

    else:
        refill_liters = int(command.split()[1])
        dispenser += refill_liters
