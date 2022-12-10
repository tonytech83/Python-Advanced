original_str = input()

# list as a stack
s = []

# push
for char in original_str:
    s.append(char)

reversed_str = ''

# peek
while s:
    reversed_str += s.pop()

print(reversed_str)
