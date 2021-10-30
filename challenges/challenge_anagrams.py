def is_anagram(first_string, second_string):
    if not first_string:
        return False

    if not second_string:
        return False

    reverse_word = first_string[::-1]

    if second_string != reverse_word:
        return False

    return True
