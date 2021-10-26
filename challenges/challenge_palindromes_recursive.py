def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) == 1:
        return True
    if low_index == high_index + 2:
        if word[high_index] == word[low_index]:
            return True
        else:
            return False

    if word[high_index] == word[low_index]:
        if low_index + 1 == high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
