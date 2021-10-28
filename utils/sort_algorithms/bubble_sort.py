def bubble_sort(list):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(list) - num_of_iterations - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                has_swapped = True
        num_of_iterations += 1

    return list
