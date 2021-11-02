def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_array = []
    second_array = []

    for letter in first_string:
        first_array.append(letter)
    for letter in second_string:
        second_array.append(letter)

    return count_letters(first_array, second_array)


def count_letters(first_array, second_array):
    index = 0

    while(index < len(first_array)):
        for letter in second_array:
            if(first_array[index] == letter):
                second_array.remove(letter)
        index += 1

    if (len(second_array) == 0):
        return True
    else:
        return False
