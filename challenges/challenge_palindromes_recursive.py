def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) <= 2:
        return word != "" and word[low_index] == word[high_index]
    else:
        same_letter = word[low_index] == word[high_index]
        next_word = word[low_index + 1:high_index]
        next_high_index = high_index - 2
        return is_palindrome_recursive(next_word, low_index, next_high_index) \
            if same_letter else same_letter
