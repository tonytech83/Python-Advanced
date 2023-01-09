from collections import deque


def fill_the_box(height, length, width, *args):
    """
    Func fills the box with the given cubes until the current argument equals "Finish".
    Args:
        height (int): height of the box
        length (int): length of the box
        width (int): width of the box
        args: n-times a different number of cubes with exact size 1 x 1 x 1 and a string "Finish"
    """
    box_volume = height * length * width
    cubes = deque(x for x in args)
    while True:
        cube = cubes.popleft()
        if cube == 'Finish':
            break
        box_volume -= int(cube)
        if box_volume < 0:
            cubes.appendleft(abs(box_volume))
            return f'No more free space! You have {sum([x for x in cubes if x != "Finish"])} more cubes.'
    return f'There is free space in the box. You could put {box_volume} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
