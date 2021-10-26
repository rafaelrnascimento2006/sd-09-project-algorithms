def is_palindrome_recursive(word, low_index = 0, high_index = -1):
    if not word:
        return False
    if low_index > len(word) // 2:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
