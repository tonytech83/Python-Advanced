import os


def create_file(*args):
    """
    This func creates empty file.
    """
    file_name = args[0]
    open(file_name, 'w').close()


def add_to_file(*args):
    """
    This func adds on new line received content.
    """
    file_name, content = args

    with open(file_name, 'a') as file:
        file.write(f'{content}\n')


def replace_string(*args):
    """
    This func searching string in file and replaced with new string. If file not exists prints message.
    """
    file_name, old_string, new_string = args

    try:
        with open(file_name, 'r+') as file:
            new_file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_file_content)
    except FileNotFoundError:
        print('An error occurred')


def delete_file(*args):
    """
    This func deletes file if exists else return message.
    """
    file_name = args[0]

    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


END_COMMAND = 'End'

while True:
    line = input()
    if line == END_COMMAND:
        break

    command, *data = line.split('-')

    commands = {
        'Create': create_file,
        'Add': add_to_file,
        'Replace': replace_string,
        'Delete': delete_file,
    }

    commands[command](*data)
