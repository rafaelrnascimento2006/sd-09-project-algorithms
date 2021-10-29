def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if word[::-1] != word:
        return False
    if word[0] == word[-1]:
        return True
    return is_palindrome_recursive(word, low_index, high_index)
