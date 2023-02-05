def start_spring(**kwargs):
    reversed_data = {}
    for key, value in kwargs.items():
        if value not in reversed_data:
            reversed_data[value] = []
        reversed_data[value].append(key)

    result = []

    for key, values in sorted(reversed_data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result.append(f'{key}:')
        for item in sorted(values):
            result.append(f'-{item}')

    return '\n'.join(result)


# Test code 1
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

# Test code 2
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

# Test code 3
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
