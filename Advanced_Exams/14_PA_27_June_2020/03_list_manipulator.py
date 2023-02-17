# Exam: 03. List Manipulator
# From: Python Advanced Exam - 27 June 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2456#2

def list_manipulator(lst, command, where, *others):
    if command == 'add':
        lst = lst + list(others) if where == 'end' else list(others) + lst

    elif command == 'remove':
        if where == 'beginning':
            lst = lst[others[0]:] if others else lst[1:]
        else:
            lst = lst[:3 - others[0]] if others else lst[:-1]

    return lst


# Test codes
print(list_manipulator([1, 2, 3], "remove", "end", 3))
print(list_manipulator([1, 2, 3], "remove", "beginning", 3))
print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
