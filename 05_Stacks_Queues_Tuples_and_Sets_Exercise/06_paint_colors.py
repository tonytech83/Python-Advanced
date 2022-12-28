from collections import deque

string = deque(x for x in input().split())

# create set to store main colors
main_colors = {'red', 'yellow', 'blue'}

# create dict to store secondary colors and their ingredients
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

formed_colors = []

while string:

    first = string.popleft()
    last = string.pop() if string else ''

    if first + last in main_colors or first + last in secondary_colors:
        color = first + last
        formed_colors.append(color)
    elif last + first in main_colors or last + first in secondary_colors:
        color = last + first
        formed_colors.append(color)
    else:
        middle = len(string) // 2
        string.insert(middle, first[:-1])
        string.insert(middle, last[:-1])
        string = deque(x for x in string if x)

result = []

for color in formed_colors:
    if color in main_colors:
        result.append(color)
    else:
        is_collected = True
        for former_color in secondary_colors[color]:
            if former_color not in formed_colors:
                is_collected = False
                break
        if is_collected:
            result.append(color)

print(result)
