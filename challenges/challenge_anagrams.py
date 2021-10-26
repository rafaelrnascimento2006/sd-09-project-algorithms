def ordenate(string):
    array_string = list(string)

    for i in range(len(array_string) - 1):
        for j in range(len(array_string) - 1):
            if array_string[j] < array_string[i]:
                aux = array_string[i]
                array_string[i] = array_string[j]
                array_string[j] = aux

    return "".join(array_string)


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first = ordenate(first_string)
    second = ordenate(second_string)
    if first == second:
        return True
    else:
        return False

# first_string = "pedra"
# second_string = "perda"
# print(is_anagram(first_string, second_string))
