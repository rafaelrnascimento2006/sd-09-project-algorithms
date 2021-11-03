def arraySort(array):
    for firstIndex in range(len(array)):
        position = firstIndex

        for secondIndex in range(firstIndex + 1, len(array)):
            if array[position] > array[secondIndex]:
                position = secondIndex

        array[position], array[firstIndex] = (
            array[firstIndex],
            array[position],
        )

    return "".join(array)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    if first_string == second_string:
        return True

    sorted_first_string = arraySort(list(first_string.lower()))
    sorted_second_string = arraySort(list(second_string.lower()))

    if sorted_first_string == sorted_second_string:
        return True
    else:
        return False
