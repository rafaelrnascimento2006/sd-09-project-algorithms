def is_palindrome_recursive(word, low_index, high_index):
    if word is None:
        return False
    if high_index == 0:
        return True
    word_reverse = word[::-1]
    if word == word_reverse:
        return is_palindrome_recursive(word, 0, high_index - 1)
    else:
        return False
