def is_anagram(first_string, second_string):
    if (
        not (first_string and second_string)
        or (len(first_string) != len(second_string))
    ):
        return False
    for i in range(len(first_string)):
        if not first_string.count(second_string[i]):
            return False
        if not (
            second_string.count(first_string[i]) ==
            first_string.count(second_string[i])
        ):
            return False
    return True
