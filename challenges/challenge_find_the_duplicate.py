def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) <= 1:
        return False
    quickSort(nums)
    for n in range(len(nums) - 1):
        if not isinstance(nums[n], int):
            return False
        elif nums[n] < 0:
            return False
        elif nums[n] == nums[n + 1]:
            return nums[n]
    return False


#  Código baseado no quicksort do site
#  https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
def quickSort(item):
    quickSortHelper(item, 0, len(item) - 1)


def quickSortHelper(item, first, last):
    if first < last:

        splitpoint = partition(item, first, last)

        quickSortHelper(item, first, splitpoint - 1)
        quickSortHelper(item, splitpoint + 1, last)


def partition(item, first, last):
    pivotvalue = item[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and item[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while item[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = item[leftmark]
            item[leftmark] = item[rightmark]
            item[rightmark] = temp

    temp = item[first]
    item[first] = item[rightmark]
    item[rightmark] = temp

    return rightmark
