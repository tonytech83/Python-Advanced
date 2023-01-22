# using 'w' (write) mode creates a file with the given name
# if the file exists, its overwritten
with open('files/my_first_file.txt', 'w') as file:
    file.write('I just created my first file!')
