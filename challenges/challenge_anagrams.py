def is_anagram(first_string, second_string):
    if not first_string:
        return False

    if not second_string:
        return False

    reverse_first_string = first_string[::-1]
    reverse_second_string = second_string[::-1]

    if second_string == reverse_first_string:
        return True

    if first_string == reverse_second_string:
        return True

    return False
