def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """

    if (low_index <= high_index and low_index != high_index):
        if (word[low_index] == word[high_index]):
            low_index += 1
            high_index -= 1
            return is_palindrome_recursive(word, low_index, high_index)
 
        else:
            return False

    if (word != ""):
        return True

    else:
        return False
