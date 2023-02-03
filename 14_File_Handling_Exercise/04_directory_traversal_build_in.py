from os import walk

start_path = input()
files_by_ext = {}

# using build-in walk instead of recursion
for _, _, files in walk(start_path):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_by_ext:
            files_by_ext[extension] = []
        files_by_ext[extension].append(file)

with open('files/report.txt', 'w') as f:
    for ext, files in sorted(files_by_ext.items()):
        f.write(f'.{ext}\n')
        for file in sorted(files):
            f.write(f'- - - {file}\n')
