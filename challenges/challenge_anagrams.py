def quicksort(array_string, low, high):

    if len(array_string) == 1:
        return array_string

    if low < high:
        partition_index = partition(array_string, low, high)
        quicksort(array_string, low, partition_index - 1)
        quicksort(array_string, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]  # pivot

    for j in range(low, high):

        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def basics_requeriments(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    if len(first_string) != len(second_string):
        return False
    return True


def is_anagram(first_string, second_string):
    if basics_requeriments(first_string, second_string) == False:
        return False

    first_array = list(first_string)
    second_array = list(second_string)
    quicksort(second_array, 0, len(second_array) - 1)
    quicksort(first_array, 0, len(second_array) - 1)
    if second_array == first_array:
        return True
    return False


if __name__ == "__main__":
    print(is_anagram('pedra', ''))

