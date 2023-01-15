numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:                                                    # add try-except to handle Value error
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:                                      #
        print('The variable number must be an integer')     #
    line = input()                                          # missing line of code

line = input()
while line != "Remove":
    searched = line
    try:                                                    # add try-except to handle Key error
        print(numbers_dictionary[searched])
    except KeyError:                                        #
        print('Number does not exist in dictionary')        #
    line = input()                                          # missing line of code

line = input()
while line != "End":
    searched = line
    try:                                                    # add try-except to handle Key error
        del numbers_dictionary[searched]
    except KeyError:                                        #
        print('Number does not exist in dictionary')        #
    line = input()                                          # missing line of code

print(numbers_dictionary)
