def reverse_word(word):
    if len(word) < 2:
        return word
    else:
        return reverse_word(word[1:]) + word[0]


def is_palindrome_recursive(word, _low_index, _high_index):
    if not word:
        return False
    elif word == reverse_word(word):
        return True
    else:
        return False
