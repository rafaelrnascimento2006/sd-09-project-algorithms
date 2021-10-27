def recursive_reverse(list):
    if not list:
        return list
    return [list[-1]] + recursive_reverse(list[:len(list)-1])


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    word = list(word)
    reverse_word = recursive_reverse(word)
    return word == reverse_word
