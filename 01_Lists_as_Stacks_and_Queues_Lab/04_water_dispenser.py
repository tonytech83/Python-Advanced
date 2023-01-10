from collections import deque


def add_people_in_queue():
    """
    Reads person name and added it in people queue while received 'Start'.
    """
    queue = deque()
    while True:
        current_name = input()

        if current_name == COMMAND_START:
            break
        queue.append(current_name)

    return queue


# constants
COMMAND_END = 'End'
COMMAND_START = 'Start'
COMMAND_REFILL = 'refill'

# received quantity of water from console input
dispenser = int(input())

# create queue to store persons
people = add_people_in_queue()

# brings water to person in the left of queue or refill the dispenser, while received 'End'.
while True:
    command = input()
    if command == COMMAND_END:
        print(f'{dispenser} liters left')
        break

    # if command is refill adds liters to dispenser
    if command.split()[0] == COMMAND_REFILL:
        refill_liters = int(command.split()[1])
        dispenser += refill_liters

    else:
        liters = int(command)
        person = people.popleft()

        # if water in dispenser is enough quantity, remove quantity from dispenser and  remove the person
        # else only remove the person from queue
        if dispenser >= liters:
            print(f'{person} got water')
            dispenser -= liters
        else:
            print(f'{person} must wait')
