def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if len(word) == 1:
        return True
    if low_index == high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    if low_index == high_index - 1 and word[low_index] == word[high_index - 1]:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
