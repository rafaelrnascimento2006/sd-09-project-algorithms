def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == '' or second_string == '':
        return False

    arrayed_first = list(first_string)
    arrayed_second = list(second_string)

    quicksort(arrayed_first, 0, len(arrayed_first) - 1)
    quicksort(arrayed_second, 0, len(arrayed_second) - 1)

    return (arrayed_first == arrayed_second)
