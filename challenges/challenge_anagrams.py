def bubbleSort(list):
    length = len(list)
    for index in range(length-1):
        for index2 in range(0, length-index-1):
            if list[index2] > list[index2 + 1]:
                list[index2], list[index2 + 1] = list[index2 + 1], list[index2]


def is_anagram(first_string, second_string):
    list1 = list(first_string)
    list2 = list(second_string)
    if list1 == list2:
        return True
    else:
        bubbleSort(list1)
        bubbleSort(list2)
    if list1 == list2:
        return True
    return False
