def create_fib_seq(n):
    """
    Creates fibonacci sequence by received number 'n'.
    """
    seq = [0, 1]

    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])

    return seq


def locate_number(sequence, n):
    """
    Locates index of received number in fibonacci sequence if exists
    """
    try:
        idx = sequence.index(n)
        return idx
    except ValueError:
        raise ValueError
