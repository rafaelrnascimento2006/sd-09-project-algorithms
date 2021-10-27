def is_anagram(first_string, second_string):
    strings_is_anagram = False

    if len(first_string) != len(second_string):
        return False

    for letter in first_string:
        if letter in second_string:
            strings_is_anagram = True
        else:
            strings_is_anagram = False
            break

        # https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
        letter_position = second_string.find(letter)
        second_string = (
            second_string[:letter_position] +
            '' + second_string[letter_position+1:])
    return strings_is_anagram
