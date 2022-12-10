# initialize empty stack
stack = []

queries_count = int(input())

for _ in range(queries_count):
    query = [int(x) for x in input().split()]
    command = query[0]

    if command == 1:
        number_to_add = query[1]
        stack.append(number_to_add)

    elif stack:
        if command == 2:
            stack.pop()

        elif command == 3:
            print(max(stack))

        else:  # command == 4
            print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(*reversed_stack, sep=', ')
