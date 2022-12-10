from collections import deque

# received quantity of water from console input
dispenser = int(input())

# create queue to store persons
people = deque()

# read person name and added it in people queue while received 'Start'
while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

# brings water to person in the left of queue or refill the dispenser, while received 'End'.
while True:
    command = input()
    if command == 'End':
        print(f'{dispenser} liters left')
        break

    if command.isdigit():

        liters = int(command)
        person = people.popleft()

        # if water in dispenser is enough quantity, remove quantity from dispenser and  remove the person
        # else only remove the person from queue
        if dispenser >= liters:
            print(f'{person} got water')
            dispenser -= liters
        else:
            print(f'{person} must wait')

    # if command is refill adds liters to dispenser
    else:
        refill_liters = int(command.split()[1])
        dispenser += refill_liters
