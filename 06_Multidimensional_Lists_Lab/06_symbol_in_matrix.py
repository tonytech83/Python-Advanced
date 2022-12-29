def read_matrix():
    """
    This func returns matrix with passed from console size and rows.
    """
    size = int(input())
    return [list(input()) for _ in range(size)]


def search_symbol(sym):
    """
    This func searches specific symbol in matrix. If founds coincidence returns its coordinates else
    returns '{symbol} does not occur in the matrix'
    """
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == sym:
                return row_idx, col_idx
    return f'{sym} does not occur in the matrix'


matrix = read_matrix()
symbol = input()
print(search_symbol(symbol))
