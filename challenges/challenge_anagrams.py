def is_anagram(first_string, second_string):
    if (
        not (first_string and second_string)
        or (len(first_string) != len(second_string))
    ):
        return False
    for n in range(len(first_string)):
        if not first_string.count(second_string[n]):
            return False
        if not (
            second_string.count(first_string[n]) ==
            first_string.count(second_string[n])
        ):
            return False
    return True
