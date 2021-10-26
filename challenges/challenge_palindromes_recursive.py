def is_palindrome_recursive(word, low_index, high_index):
    # https://www.w3schools.com/python/ref_string_isalpha.asp
    if (word.isalpha()):
        if (high_index < low_index):
            return True
        else:
            if (word[low_index] == word[high_index]):
                return is_palindrome_recursive(
                    word, low_index + 1, high_index - 1
                )
            else:
                return False
    return False
