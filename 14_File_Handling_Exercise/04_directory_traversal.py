import os


def read_directory(current_directory: str):
    """
    This func traverses the first level of the directory only and adds information about each found file in dict.
    """
    files = [item for item in os.listdir(current_directory) if os.path.isfile(item)]

    current_extensions = {}

    for file in files:
        extension = file.split('.')[-1]
        if extension not in current_extensions:
            current_extensions[extension] = []
        current_extensions[extension].append(file)

    return current_extensions


def create_report(extensions: dict):
    """
    This func writes information about each file form extensions dict in report.txt
    """
    with open('report.txt', 'w') as f:
        for extension, files in sorted(extensions.items()):
            f.write(f'.{extension}\n')
            for file in sorted(files):
                f.write(f'- - - {file}.{extension}\n')


directory = input()

found_extensions = read_directory(directory)
create_report(found_extensions)
