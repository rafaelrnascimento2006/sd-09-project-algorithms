def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
    if len(word) == 1:
        return True
    return is_palindrome_recursive(word[1: high_index], 0, -1)
