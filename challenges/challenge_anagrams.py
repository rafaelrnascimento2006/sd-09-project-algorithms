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
    first_sorted = list(first_string)
    second_sorted = list(second_string)
    quicksort(first_sorted, 0, len(first_sorted) - 1)
    quicksort(second_sorted, 0, len(second_sorted) - 1)
    if first_sorted == second_sorted:
        return True
    else:
        return False
