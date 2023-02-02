import os


def traverse_dir(current_path):
    """
    This func traverses the directory, it's child directories and adds information about each found file in dict.
    """
    global found_extensions

    for element in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, element)):
            traverse_dir(os.path.join(current_path, element))
        else:
            extension = element.split('.')[-1]

            if extension not in found_extensions:
                found_extensions[extension] = []
            found_extensions[extension].append(element)


def create_report(extensions: dict):
    """
    This func writes information about each file form extensions dict in report.txt
    """
    with open('report.txt', 'w') as f:
        for extension, files in sorted(extensions.items()):
            f.write(f'.{extension}\n')
            for file in sorted(files):
                f.write(f'- - - {file}\n')


start_path = input()
found_extensions = {}
traverse_dir(start_path)
create_report(found_extensions)
