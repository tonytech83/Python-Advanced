# Exam: 03. Numbers Search
# From: Python Advanced Retake Exam - 19 August 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2463#2

def numbers_searching(*args):
    missing_num = 0
    duplicates_found = []

    for num in range(min(args), max(args) + 1):
        if num not in args:
            missing_num = num
        elif args.count(num) > 1:
            duplicates_found.append(num)

    return [missing_num, duplicates_found]


# Test code 1
print(numbers_searching(1, 2, 4, 2, 5, 4))

# Test code 2
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

# Test code 3
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
