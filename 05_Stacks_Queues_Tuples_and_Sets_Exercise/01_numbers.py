def add_number(data):
    global first
    global second

    where = data[0]
    new_numbers = set(int(x) for x in data[1:])

    if where == 'First':
        first = first.union(new_numbers)
    else:
        second = second.union(new_numbers)


def remove_number(data):
    global first
    global second

    where = data[0]
    remove_numbers = set(int(x) for x in data[1:])

    if where == "First":
        first = first.difference(remove_numbers)
    else:
        second = second.difference(remove_numbers)


def check_subset():
    if first.issubset(second) or second.issubset(first):
        return 'True'
    return 'False'


first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    event, *data = input().split()

    if event == 'Add':
        add_number(data)

    elif event == 'Remove':
        remove_number(data)

    elif event == 'Check':
        print(check_subset())

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
