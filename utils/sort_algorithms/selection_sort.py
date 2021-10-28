def selection_sort(list):
    for i in range(len(list)):
        minimum = i

        for j in range(i + 1, len(list)):
            if list[j] < list[minimum]:
                minimum = j
        list[minimum], list[i] = list[i], list[minimum]

    return list
