import os


def extract_extensions(current_directory: str, first_level=False):
    """
    This func traverses root directory and all first level directories.
    Writes information about each found file to found_extensions dict.
    """
    global found_extensions

    for element in os.listdir(current_directory):
        path = os.path.join(current_directory, element)

        if os.path.isfile(path):
            extension = element.split('.')[-1]

            if extension not in found_extensions:
                found_extensions[extension] = []

            found_extensions[extension].append(element)

        elif os.path.isdir(element):
            extract_extensions(path, first_level=True)

        elif first_level:
            break


def create_report(extensions: dict):
    """
    This func writes information about each file form extensions dict in report.txt
    """
    with open('files/report.txt', 'w') as f:
        for extension, files in sorted(extensions.items()):
            f.write(f'.{extension}\n')
            for file in sorted(files):
                f.write(f'- - - {file}\n')


directory = input()

found_extensions = {}
extract_extensions(directory)
create_report(found_extensions)
