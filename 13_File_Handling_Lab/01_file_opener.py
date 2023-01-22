import os

# take the absolute path to the directory where is stored .py file
absolute_path = os.path.dirname(os.path.abspath(__file__))

# take the path to file which want ot open with os.path.join (works for all OS types)
file_path = os.path.join(absolute_path, 'files', 'text.txt')

try:
    file_obj = open(file_path)
    print('File found')
except FileNotFoundError:
    print('File not found')
