def is_palindrome_recursive(word, low_index, high_index):
    print(word, type(word))
    if not word:
        return False
    if word[low_index] != word[high_index]:
        return False
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(low_index + 1, high_index - 1)


print(is_palindrome_recursive('', 0, 2))
