def sort_array(array):
    for index in range(len(array)):
        prev = index

        for curr in range(index + 1, len(array)):
            if array[curr] < array[prev]:
                prev = curr

        array[prev], array[index] = array[index], array[prev]

    return array


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    first_string = sort_array(list(first_string))
    second_string = sort_array(list(second_string))

    # print(first_string)
    # print(second_string)
    return first_string == second_string


print(is_anagram('tsete', 'setet'))
