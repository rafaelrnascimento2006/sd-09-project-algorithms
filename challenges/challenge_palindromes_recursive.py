def is_palindrome_recursive(word, low_index, high_index):
    if word:
        if high_index < low_index:
            return True
        else:
            if word[low_index] == word[high_index]:
                return is_palindrome_recursive(
                    word, low_index + 1, high_index - 1
                )
            else:
                return False
    return False
