text = input()

chars_dict = {}

for char in text:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1

# we can use:
# 'for character, count in sorted(chars_dict.items())'
# because sorted func always sort on first element of kvp.
for character, count in sorted(chars_dict.items(), key=lambda kvp: kvp[0]):
    print(f'{character}: {count} time/s')
