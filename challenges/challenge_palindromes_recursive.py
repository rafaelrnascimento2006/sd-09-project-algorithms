def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif high_index == 0:
        return True
    reverse_word = word[::-1]
    if word == reverse_word:
        return is_palindrome_recursive(word, 0, high_index - 1)
    else:
        return False
