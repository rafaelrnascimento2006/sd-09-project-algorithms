def is_palindrome_recursive(word, low_index, high_index):
    if low_index < len(word) / 2:
        if not word:
            return False
        if word[low_index] != word[high_index]:
            return False
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True


# https://academiahopper.com.br/recursao-python/
