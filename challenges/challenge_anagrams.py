def is_anagram(first_string, second_string):
    len_first = len(first_string)
    len_second = len(second_string)
    if (not first_string or not second_string) and (len_first != len_second):
        return False

    for letter_first in first_string:
        for letter_second in second_string:
            if letter_first == letter_second:
                first_string = first_string.replace(letter_first, "")
                second_string = second_string.replace(letter_second, "")
    if len(first_string) == 0 and len(second_string) == 0:
        return True


# is_anagram('asd', 'sda')
