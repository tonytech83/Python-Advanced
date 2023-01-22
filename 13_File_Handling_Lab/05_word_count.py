import re


def read_searched_words():
    """
    This func reads words file in file_path with searched words.
    """
    file_path = 'files/words.txt'
    with open(file_path) as file:
        searched_words = [word for word in file.readline().split()]
    return searched_words


def find_words_count():
    """
    This func reads input.txt file form file_path and create dict with words form searched_words as key and
    count how many times contained in input.txt as value.
    """
    searched_words = read_searched_words()
    file_path = 'files/input.txt'
    words_count = {}
    with open(file_path) as file:
        input_text = file.read()
        for word in searched_words:
            pattern = rf'\b{word}\b'
            count = len(re.findall(pattern, input_text, re.I))
            words_count[word] = count

    return words_count


def write_result_to_file():
    """
    This func written words sorted by frequency in descending order in output.txt in file_path.
    """
    file_path = 'files/output.txt'
    with open(file_path, 'w') as file:
        for word, count in sorted(find_words_count().items(), key=lambda kvp: -kvp[1]):
            file.write(f'{word} - {count}\n')


write_result_to_file()
