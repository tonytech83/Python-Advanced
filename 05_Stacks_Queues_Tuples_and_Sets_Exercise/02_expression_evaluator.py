from collections import deque

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

string_expression = input().split()
evaluation = deque()

for symbol in string_expression:
    if symbol in '+-*/':
        while len(evaluation) > 1:
            left = evaluation.popleft()
            right = evaluation.popleft()
            result = operators[symbol](left, right)
            evaluation.appendleft(result)
    else:
        evaluation.append(int(symbol))

print(*evaluation)
