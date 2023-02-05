from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}
found_word = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(vowel, '')
        words[word] = words[word].replace(consonant, '')
        if words[word] == '':
            print(f'Word found: {word}')
            found_word = True

    if found_word:
        break

if not found_word:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
