def output(n, idx):
    """
    Prints number and its index if number exists else only number.
    """
    if not idx:
        print(f'The number {n} is not in the sequence')
    else:
        print(f'The number - {n} is at index {idx}')
