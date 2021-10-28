def insertion_sort(list):
    for index in range(len(list)):
        curr_value = list[index]
        curr_position = index
        while (
            curr_position > 0
            and list[curr_position - 1] > curr_value
        ):
            list[curr_position] = list[curr_position - 1]
            curr_position = curr_position - 1
        list[curr_position] = curr_value
    return list
