def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if (first_string[:2] == second_string[:2]
            and first_string[-2:] == second_string[-2:]):
        return True

    inverted_first = (first_string[-3:-1][1], first_string[-3:-1][0])
    inverted_second = (second_string[-3:-1][0], second_string[-3:-1][1])

    if inverted_first != inverted_second:
        return False

    return True
