def is_palindrome_recursive(word, low_index, high_index):
    if (not len(word)):
        return False

    if (low_index == high_index or low_index > high_index):
        return True

    if (word[low_index] != word[high_index]):
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# print(is_palindrome_recursive('OVO', 0, len('OVO') - 1))
