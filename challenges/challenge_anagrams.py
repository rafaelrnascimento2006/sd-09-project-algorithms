from challenges.merge_sort import merge_sort


# Os únicos algoritmos de ordenação que é certeza que vamos
# ter no maximo O(n*log n) são: o merge sort (mais estável)
# heap sort e o 'tim sort'
def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_sorted = merge_sort(first_string)
    second_sorted = merge_sort(second_string)

    for index in range(0, len(first_sorted)):
        if not first_sorted[index] == second_sorted[index]:
            return False
    return True
