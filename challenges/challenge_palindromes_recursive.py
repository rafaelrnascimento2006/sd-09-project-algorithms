def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
# https://www.demo2s.com/python/python-check-palindrome-using-recursive-function.html
# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
# https://www.sanfoundry.com/python-program-check-string-palindrome-using-recursion/

    if not word:
        return False

    # if (len(word) <= 2 and len(word) > 0):
    #     return True ====== deveria funcionar!

    if (low_index >= high_index):
        return True

    #  If the last letter is equal to the first letter, the function is called
    #  recursively with the argument as the sliced list with the first
    #  character and last character removed, else return False.
    if (word[low_index] == word[high_index]):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
