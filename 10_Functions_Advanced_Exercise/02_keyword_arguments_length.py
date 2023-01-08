def kwargs_length(**kwargs):
    return len(kwargs)


# Test codes
print(kwargs_length(**{'name': 'Peter', 'age': 25}))
print(kwargs_length(**{}))
