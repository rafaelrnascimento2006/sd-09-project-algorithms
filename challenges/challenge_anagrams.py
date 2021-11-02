# Requisito 03
def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    if first_string == second_string:
        return True

    sorted_first_string = sorted_array(list(first_string.lower()))
    sorted_second_string = sorted_array(list(second_string.lower()))

    if sorted_first_string == sorted_second_string:
        return True
    else:
        return False


# transformamos a string num array
# ordenamos de forma alfabética
# retorna uma string
def sorted_array(array):
    for index1 in range(len(array)):
        position = index1

        for index2 in range(index1 + 1, len(array)):
            if array[position] > array[index2]:
                position = index2

        array[position], array[index1] = (
            array[index1],
            array[position],
        )

    return "".join(array)
