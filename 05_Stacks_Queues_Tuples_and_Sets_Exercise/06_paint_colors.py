from collections import deque

string = deque(x for x in input().split())

# create set to store main colors
main_colors = {'red', 'yellow', 'blue'}

# create dict to store secondary colors and their ingredients
secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
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
        for el in (first[:-1], last[:-1]):
            if el:
                string.insert(middle, el)

result = []

# takes only secondary colors which have in formed colors and checks
# if the value (set) of this color is subset of formed colors (have needed colors to create secondary color).
for color in set(secondary_colors.keys()).intersection(formed_colors):
    if not secondary_colors[color].issubset(formed_colors):
        formed_colors.remove(color)

print(formed_colors)
