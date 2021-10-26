def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    first_string = list(first_string)
    second_string = list(second_string)

    for index in range(1, len(first_string)):
        next_elem_first = first_string[index]
        next_elem_second = second_string[index]

        prev_index_first = index - 1
        prev_index_second = index - 1

        while True:
            if next_elem_first < first_string[prev_index_first] and prev_index_first >= 0:
                first_string[prev_index_first +
                             1] = first_string[prev_index_first]
                prev_index_first -= 1

            elif next_elem_second < second_string[prev_index_second] and prev_index_second >= 0:
                second_string[prev_index_second +
                              1] = second_string[prev_index_second]
                prev_index_second -= 1

            else:
                break

        first_string[prev_index_first + 1] = next_elem_first
        second_string[prev_index_second + 1] = next_elem_second

    # print(first_string)
    # print(second_string)

    # while prev_index_second >= 0 and next_elem_second < second_string[prev_index_second]:
    #     second_string[prev_index_second +
    #                   1] = second_string[prev_index_second]
    #     prev_index_second -= 1

    # second_string[prev_index_second + 1] = next_elem_second

    # for index in range(1, len(second_string)):
    #     next_elem_second = second_string[index]

    #     prev_index = index - 1

    #     while prev_index >= 0 and next_elem_second < second_string[prev_index]:
    #         second_string[prev_index + 1] = second_string[prev_index]
    #         prev_index -= 1

    #     second_string[prev_index + 1] = next_elem_second

    return first_string == second_string


is_anagram('tsete', 'setet')
