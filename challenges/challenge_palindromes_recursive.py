def is_palindrome_recursive(word, low_index, high_index):
    word_is_empty = len(word) == 0
    word_is_a_letter = len(word) == 1

    if word_is_a_letter:
        return True
    if word_is_empty:
        return False
    if word[low_index] != word[high_index]:
        return False
    if (word[low_index] == word[high_index]) and (
            low_index != high_index) and (high_index > 0):
        return is_palindrome_recursive(word, low_index+1, high_index-1)
    return True
