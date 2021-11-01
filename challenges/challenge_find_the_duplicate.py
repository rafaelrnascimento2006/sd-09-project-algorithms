def find_duplicate(nums):
    sortedNums = merge_sort(nums)
    for i in range(0, len(sortedNums)):
        if not isinstance(sortedNums[i], int):
            return False
        if sortedNums[i] <= 0:
            return False
        if i+1 != sortedNums[i]:
            return sortedNums[i]
    return False


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


nums = [3, 1, 3, 4, 2]
# 3
print(find_duplicate(nums))


nums = [1, 1]
# saída: 1
print(find_duplicate(nums))


nums = [1, 1, 2]
# saída: 1
print(find_duplicate(nums))

nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# saída: 7
print(find_duplicate(nums))
