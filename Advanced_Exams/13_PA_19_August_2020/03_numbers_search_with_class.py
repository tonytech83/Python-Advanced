# Exam: 03. Numbers Search
# From: Python Advanced Retake Exam - 19 August 2020
# URL: https://judge.softuni.org/Contests/Practice/Index/2463#2

# Solution with class for training

class SearchNumbers:
    def __init__(self, *args):
        self.data = args
        self.duplicates_found = []
        self.missing_number = 0

    def find_missing_number(self):
        full_range = set(range(min(self.data), max(self.data) + 1))
        data_range = set(self.data)

        self.missing_number = full_range - data_range

    def find_duplicates(self):
        self.duplicates_found = sorted(set(num for num in self.data if self.data.count(num) > 1))

    def return_result(self):
        return [*self.missing_number, list(self.duplicates_found)]


def numbers_searching(*args):
    result = SearchNumbers(*args)
    result.find_missing_number()
    result.find_duplicates()
    return result.return_result()


# Test code 1
print(numbers_searching(1, 2, 4, 2, 5, 4))

# Test code 2
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

# Test code 3
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
