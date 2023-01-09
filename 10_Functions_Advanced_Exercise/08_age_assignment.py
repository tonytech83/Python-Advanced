def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            age = kwargs[first_letter]
            persons[name] = age
    sorted_persons = [f'{n} is {a} years old.' for n, a in sorted(persons.items(), key=lambda kvp: kvp[0])]
    return '\n'.join(sorted_persons)


# Test codes
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
