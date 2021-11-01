def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if _is_anagram(first_string) == _is_anagram(second_string):
        return True
    else:
        return False


def _is_anagram(string):
    condition = True
    string = list(string)
    counter = 0
    while condition:
        condition = False

        for index in range(len(string) - counter - 1):
            if string[index] > string[index+1]:
                string[index], string[index+1] = string[index+1], string[index]
                condition = True

        counter += 1

    return "".join(string)
