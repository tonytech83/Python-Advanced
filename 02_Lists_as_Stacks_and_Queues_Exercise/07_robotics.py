from collections import deque


def read_robots():
    """
    Split the input (for example: ROB-15;SS2-10;NX8000-3) by ';' to take robot information.
    Split the robot information to name and processing time and put the as key-value in current_robots dict.
    :return: dict
    """
    current_robots = {}
    line = input().split(';')

    for robot in line:
        name, process_time = robot.split('-')
        current_robots[name] = int(process_time)
    return current_robots


def read_items():
    """
    This func read lines one by one and store them in queue.
    :return: deque
    """
    current_items = deque()
    line = input()

    while line != 'End':
        current_items.append(line)
        line = input()

    return current_items


def robot_time_decrease():
    """
    This func decrease time for any robot in working_robots dict for each loop of the assembly line.
    If process time of current robot goes to 0, remove the robot from working_robots dict and
    add it to available_robots list.
    """
    global working_robots
    global available_robots

    # we are using list from working.keys(), because if we iterate through working_robots and remove item from it
    # on some iteration, we will receive exception.
    for robot in [r for r in working_robots.keys()]:
        working_robots[robot] -= 1
        if working_robots[robot] == 0:
            del working_robots[robot]
            available_robots.append(robot)


def to_time(secs):
    """
    This function convert second to hh:mm:ss format.
    :param secs: int
    :return: str
    """
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = (secs % 3600) % 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()

# create list with names of all robots. It will store only available robots
available_robots = [r for r in robots.keys()]

# the dict will store robots which start work on item.
working_robots = {}

time_str = input().split(':')

# convert string time to seconds
time_in_seconds = int(time_str[0]) * 60 * 60 + int(time_str[1]) * 60 + int(time_str[2])

items = read_items()

while items:
    current_item = items.popleft()
    time_in_seconds += 1

    # call function to reduce the time for robots in working_robots dict, for each loop.
    robot_time_decrease()

    # if time reach 86400 seconds (24:00:00), reset the time to 0 seconds (00:00:00)
    if time_in_seconds == (24 * 60 * 60):
        time_in_seconds = 0

    for robot_name in available_robots:
        if robot_name not in working_robots:
            print(f'{robot_name} - {current_item} [{to_time(time_in_seconds)}]')
            working_robots[robot_name] = robots[robot_name]
            break
    else:
        items.append(current_item)
