import re
from string import punctuation

input_path = 'files/text.txt'
output_path = 'files/output.txt'

with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    for idx, line in enumerate(input_file):
        stripped_line = line.strip()
        letters_count = len(re.findall('[A-Za-z]', stripped_line))
        punctuations_count = len([char for char in stripped_line if char in punctuation])
        output_file.write(f'Line {idx + 1}: {stripped_line} ({letters_count})({punctuations_count})\n')
