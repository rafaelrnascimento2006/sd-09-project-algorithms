def is_palindrome_recursive(word, low_index, high_index):
    # word_is_even = len(word) % 2 == 0
    word_is_empty = len(word) == 0

    if len(word) == 1:
        return True
    if word_is_empty:
        return False
    if word[low_index] != word[high_index]:
        return False
    if word[low_index] == word[high_index] and low_index != high_index and high_index > 0:
        is_palindrome_recursive(word, low_index+1, high_index-1)
    print('é palindromo')
    return True
