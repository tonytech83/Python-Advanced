def palindrome(word, idx):
    """
    Recursive function that will receive a word and an index (always 0). Implement the function,
    so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome"
    if the word is not a palindrome using recursion.

    Args:
        word (str): text witch should be checked
        idx (int): the index from which the checks should start
    """
    # REQUIRED -> base case where recursion should stop
    if idx >= len(word) // 2:
        return f'{word} is a palindrome'

    left = word[idx]
    right = word[-1 - idx]

    if left != right:
        return f'{word} is not a palindrome'

    return palindrome(word, idx + 1)


# test cases
print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome('abcdba', 0))
