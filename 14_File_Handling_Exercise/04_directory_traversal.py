import os


def read_directory(current_directory: str):
    """
    This func traverses the first level of the directory only and adds information about each found file in dict.
    """
    files = [item for item in os.listdir(current_directory) if os.path.isfile(item)]

    current_extensions = {}

    for file in files:
        name, extension = file.split('.')
        if extension not in current_extensions:
            current_extensions[extension] = []
        current_extensions[extension].append(name)

    return current_extensions


def create_report(extensions: dict):
    """
    This func writes information about each file form extensions dict in report.txt
    """
    with open('report.txt', 'w') as file:
        for extension, names in sorted(extensions.items()):
            file.write(f'.{extension}\n')
            for name in sorted(names):
                file.write(f'- - - {name}.{extension}\n')


directory = input()

found_extensions = read_directory(directory)
create_report(found_extensions)
