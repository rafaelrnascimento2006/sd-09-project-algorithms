# Trecho de código inspirado no course da Trybe

def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        partition_index = partition(arr, low, high)
        quicksort(arr, low, partition_index - 1)
        quicksort(arr, partition_index + 1, high)


def partition(arr, low, high):
    index = low - 1
    pivot = arr[high]
    for each_element in range(low, high):
        if arr[each_element] <= pivot:
            index += 1
            arr[index], arr[each_element] = arr[each_element], arr[index]
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1

# Lógica da seguinte função inspirada no PR:
# https://github.com/tryber/sd-09-project-algorithms/pull/72/files

def is_anagram(first_string, second_string):
    first_str_array = list(first_string)
    second_str_array = list(second_string)
    quicksort(first_str_array, 0, len(first_str_array) - 1)
    quicksort(second_str_array, 0, len(second_str_array) - 1)
    if first_str_array == second_str_array:
        return True
    else:
        return False
