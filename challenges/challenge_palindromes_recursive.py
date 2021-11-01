def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) == 1:
        return True

    if word[low_index] == word[high_index]:
        if low_index+1 == high_index or low_index+2 == high_index:
            return True
        return is_palindrome_recursive(word, low_index+1, high_index-1)
    else:
        return False
