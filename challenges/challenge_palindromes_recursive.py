def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if word[high_index] == word[low_index]:
        return True
    return False
