# Exam: 03. Naughty or Nice
# From: Python Advanced Retake Exam - 15 December 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/3306#2
def naughty_or_nice_list(kids, *args, **kwargs):
    sorted_kids = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }

    if args:
        for command in args:
            counting_number = 0
            found_name = []
            number, kid_type = command.split('-')
            kid_to_remove = 0

            for kid_info in kids:
                kid_number, name = kid_info

                if int(number) == kid_number:
                    counting_number += 1
                    found_name.append(name)
                    kid_to_remove = kids.index(kid_info)

            if counting_number == 1:
                sorted_kids[kid_type].append(found_name.pop())
                kids.pop(kid_to_remove)

    if kwargs:
        for name, kid_type in kwargs.items():
            counting_number = 0
            found_name = []

            for kid_info in kids:
                kid_name = kid_info[1]

                if kid_name == name:
                    counting_number += 1
                    found_name.append(name)
                    kid_to_remove = kids.index(kid_info)

            if counting_number == 1:
                sorted_kids[kid_type].append(found_name.pop())
                kids.pop(kid_to_remove)

    if kids:
        for num, non_found_kid in kids:
            sorted_kids['Not found'].append(non_found_kid)

    result = ''
    for kid_type, kids in sorted_kids.items():
        if kids:
            result += f'{kid_type}: {", ".join(kids)}\n'

    return result


# Test code 1
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# Test code 2
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

# Test code 3
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
