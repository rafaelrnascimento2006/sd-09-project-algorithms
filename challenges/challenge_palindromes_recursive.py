def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    x = (word[::-1] == word, low_index)
    if x[1] >= 1:
        return x[0]
    return is_palindrome_recursive(word, low_index + 1, high_index)
