def is_palidrome_and_is_not_empty(word, is_palidrome):
    if word != '' and is_palidrome:
        return True
    return False


def is_palindrome_recursive(word, low_index, high_index):
    is_palidrome = True
    if low_index < len(word) and high_index < len(word):
        if (low_index != high_index) and (word[low_index] == word[high_index]):
            if is_palindrome_recursive(word, low_index + 1, high_index - 1):
                return True
            return False 
        else:
            if word[low_index] != word[high_index] or len(word) == 0:
                is_palidrome = False

    return is_palidrome_and_is_not_empty(word, is_palidrome)


if __name__ == "__main__":
    words = ''
    print(is_palindrome_recursive(words, 0, len(words) - 1))
