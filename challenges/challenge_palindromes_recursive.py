def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    elif word[low_index] == word[high_index]:
        if low_index < high_index - 1:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return True
    else:
        return False
