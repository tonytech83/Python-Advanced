from collections import deque

sequence_parentheses = input()

pairs_dict = {
    '(': ')',
    '{': '}',
    '[': ']'
}

parentheses_queue = deque()

balanced = True
for bracket in sequence_parentheses:
    if bracket in pairs_dict:
        parentheses_queue.append(bracket)

    elif not parentheses_queue:
        balanced = False

    else:
        last_opening_bracket = parentheses_queue.pop()
        if pairs_dict[last_opening_bracket] != bracket:
            balanced = False

    if not balanced:
        break

if balanced and not parentheses_queue:
    print('YES')
else:
    print('NO')
