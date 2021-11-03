def get_reverse_word(word):
    reverse_word_letter_list = []
    for letter in word:
        reverse_word_letter_list.insert(0, letter)
    return ''.join(reverse_word_letter_list)


def is_palindrome_iterative(word):
    if not word:
        return False
    elif word == get_reverse_word(word):
        return True
    else:
        return False
