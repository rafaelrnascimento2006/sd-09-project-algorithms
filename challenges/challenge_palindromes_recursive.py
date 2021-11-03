def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or word[low_index] != word[high_index]:
        return False
    if len(word)-1 == low_index and high_index == 0:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

