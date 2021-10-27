def is_palindrome_recursive(word, low_index, high_index):

    if high_index == low_index:
        return True

    if high_index < low_index:
        return False
        
    if (word[high_index] != word[low_index]) or  word == "":
        return False
        
    if (word[high_index] == word[low_index]):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)