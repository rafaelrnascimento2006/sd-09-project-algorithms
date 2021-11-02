def anagram(string):
    string_list = []
    for character in string.lower():
        string_list.append(character)

    string_dict = {}
    for character in string_list:
        if character not in string_dict:
            string_dict[character] = 1
        else:
            string_dict[character] = string_dict[character] + 1

    return string_dict


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    s1 = anagram(first_string)
    s2 = anagram(second_string)

    if s1 == s2:
        return True
    else:
        return False
