def is_anagram(first_string, second_string):

    if second_string == first_string:
        return True

    if second_string != first_string:
        return False

    if second_string == '' or first_string == '':
        return False
