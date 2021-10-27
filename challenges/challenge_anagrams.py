def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    string_a = list(first_string)
    string_b = list(second_string)
    quickSort(string_a)
    quickSort(string_b)
    resp = False
    for i in range(len(string_a)):
        if string_a[i] == string_b[i]:
            resp = True
        else:
            return False
    return resp


#  Código baseado no quicksort do site
#  https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
def quickSort(string):
    quickSortHelper(string, 0, len(string) - 1)


def quickSortHelper(string, first, last):
    if first < last:

        splitpoint = partition(string, first, last)

        quickSortHelper(string, first, splitpoint - 1)
        quickSortHelper(string, splitpoint + 1, last)


def partition(string, first, last):
    pivotvalue = string[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and string[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while string[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = string[leftmark]
            string[leftmark] = string[rightmark]
            string[rightmark] = temp

    temp = string[first]
    string[first] = string[rightmark]
    string[rightmark] = temp

    return rightmark
