import os

file_path = 'files/my_first_file.txt'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')

# ---- other solution with try-except ----
# try:
#     os.remove(file_path)
# except FileNotFoundError:
#     print('File already deleted!')
