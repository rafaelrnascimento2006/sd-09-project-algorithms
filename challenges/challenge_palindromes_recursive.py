def is_palindrome_recursive(word, low_index, high_index):
    # algoritmo adaptado com base na solução apresentada em
    # https://youtu.be/WPSeyjX1-4s?t=1752
    if not(word):
        return False
    if high_index - low_index < 1:
        return True
    return ((word[low_index] == word[high_index]) and (
        is_palindrome_recursive(word, low_index + 1, high_index - 1)))
