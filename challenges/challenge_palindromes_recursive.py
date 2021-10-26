def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if len(word) == 1:
        return True

    if word[low_index] == word[high_index]:
        if low_index + 1 == high_index:
            return True
        return is_palindrome_recursive(
            word[1:high_index], low_index, high_index - 2
        )
    else:
        return False
