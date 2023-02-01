def words_sorting(*words):
    words_dict = {word: sum(map(ord, word)) for word in words}

    if sum(words_dict.values()) % 2 == 1:
        result = (f'{key} - {value}' for key, value in sorted(words_dict.items(), key=lambda kvp: -kvp[1]))
    else:
        result = (f'{key} - {value}' for key, value in sorted(words_dict.items(), key=lambda kvp: kvp[0]))

    return '\n'.join(result)


# Test code 1
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
# Test code 2
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

# Test code 1
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
