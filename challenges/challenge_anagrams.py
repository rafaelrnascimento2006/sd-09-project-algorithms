def is_anagram(first_string, second_string):
    if first_string != second_string:
        return False
    elif (
        first_string[0] == second_string[0]
        and first_string[-1] == second_string[-1]
    ):
        return True
    return True
