def sorting_cheeses(**kwargs):
    """
    The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind
    in descending order. If two or more cheeses have the same number of pieces, sort them by their names in ascending
    order (alphabetically). For each kind of cheese, return their pieces quantities in descending order.
    """
    cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = []

    for cheese, pieces in cheeses:
        result.append(cheese)
        result.extend(sorted(pieces, reverse=True))

    return '\n'.join([str(x) for x in result])


# first input
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
# second input
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
