def print_up_part(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def print_bottom_part(n):
    for row in range(n - 1, 0, -1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def print_triangle(n):
    print_up_part(n)
    print_bottom_part(n)
