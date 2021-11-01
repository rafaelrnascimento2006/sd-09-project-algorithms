def is_anagram(first_string, second_string):
    return merge_sort(list(first_string)) == merge_sort(list(second_string))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right, arr.copy())


def merge(left, right, merged):
    lIndex, rIndex = 0, 0

    while lIndex < len(left) and rIndex < len(right):

        if left[lIndex] <= right[rIndex]:
            merged[lIndex + rIndex] = left[lIndex]
            lIndex += 1
        else:
            merged[lIndex + rIndex] = right[rIndex]
            rIndex += 1

    for lIndex in range(lIndex, len(left)):
        merged[lIndex + rIndex] = left[lIndex]

    for rIndex in range(rIndex, len(right)):
        merged[lIndex + rIndex] = right[rIndex]

    return merged
