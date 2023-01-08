def even_odd_filter(**kwargs):
    result_dict = {}

    for key, value in sorted(kwargs.items()):
        parity = 0 if key == 'even' else 1
        result_dict[key] = [x for x in value if x % 2 == parity]

    return dict(sorted(result_dict.items(), key=lambda kvp: -len(kvp[1])))


# Test codes
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
