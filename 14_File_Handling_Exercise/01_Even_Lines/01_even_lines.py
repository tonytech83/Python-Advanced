symbols_to_replace = ["-", ",", ".", "!", "?"]
file_path = '../02_Line_Numbers/text.txt'

with open(file_path, 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            for symbol in symbols_to_replace:
                line = line.replace(symbol, '@')
            print(' '.join(reversed(line.strip().split())))
