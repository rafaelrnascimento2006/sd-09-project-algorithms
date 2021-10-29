def is_palindrome_recursive(word, low_index, high_index):
    print(len(word), word)
    if not word:
        return False

    lower_word = word.lower()

    if (
        len(lower_word) == 2
        and lower_word[low_index] == lower_word[high_index]
        or len(lower_word) < 2
    ):
        return True

    if lower_word[low_index] != lower_word[high_index]:
        return False

    # splited_word = lower_word[low_index + 1 : high_index - 1]
    splited_word = word[low_index + 1: high_index]

    return is_palindrome_recursive(
        splited_word, low_index, len(splited_word) - 1
        )
