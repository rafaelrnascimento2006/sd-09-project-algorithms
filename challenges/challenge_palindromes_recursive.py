def is_palindrome_recursive(word, low_index, high_index):
    if low_index == high_index:
        return True
    elif word != "" and word[low_index] == word[high_index]:
        if low_index > high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False


print(is_palindrome_recursive('', 0, -1))
