# Exam: 03. Magic Triangle
# From: Python Advanced Retake Exam - 16 December 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2720#2

# Algorithm -> https://en.wikipedia.org/wiki/Pascal%27s_triangle

def get_magic_triangle(number):
    result = []

    for idx in range(number):
        new_row = [1]
        if result:
            previous_row = result[-1]

            for row in range(len(previous_row) - 1):
                new_num = previous_row[row] + previous_row[row + 1]
                new_row.append(new_num)
            new_row.append(1)
        result.append(new_row)

    return result


get_magic_triangle(5)
