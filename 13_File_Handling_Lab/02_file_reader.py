try:
    with open('files/numbers.txt') as file:
        print(sum([int(line) for line in file.readlines()]))

except FileNotFoundError:
    print('File not found!')
