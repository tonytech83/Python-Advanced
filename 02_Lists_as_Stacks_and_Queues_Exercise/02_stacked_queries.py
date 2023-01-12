# initialize empty stack
stack = []

queries_count = int(input())

query_map = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(queries_count):
    query = [int(el) for el in input().split()]
    query_map[query[0]](query)

stack.reverse()

print(*stack, sep=', ')
