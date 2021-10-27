def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    smaller_index = 0
    bigger_index = len(word) - 1
    while smaller_index < bigger_index:
        if word[smaller_index] != word[bigger_index]:
            return False
        smaller_index += 1
        bigger_index -= 1
    return True
