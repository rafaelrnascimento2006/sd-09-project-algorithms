def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)

    if len(first_list) != len(second_list):
        return False

    for letter in first_list:
        if letter not in second_list:
            return False
        else:
            return True
