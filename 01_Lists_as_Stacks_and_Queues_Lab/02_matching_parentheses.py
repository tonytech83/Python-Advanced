algebraic_xpression = input()

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

# using list for stack
s = []

for idx in range(len(algebraic_xpression)):
    if algebraic_xpression[idx] == OPEN_BRACKET:
        # push to stack index of opening bracket
        s.append(idx)
    elif algebraic_xpression[idx] == CLOSE_BRACKET:
        # pop from stack
        start_idx = s.pop()
        end_idx = idx + 1
        print(algebraic_xpression[start_idx:end_idx])
