def merge_rest_of_half_into_main(main, main_index, half, half_index):
    while half_index < len(half):
        main[main_index] = half[half_index]
        half_index += 1
        main_index += 1


def merge_halfs_into_main_list(main_list, left_half, right_half):
    left_index, right_index, main_index = 0, 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        left_item = left_half[left_index]
        right_item = right_half[right_index]

        if left_item < right_item:
            main_list[main_index] = left_item
            left_index += 1
        else:
            main_list[main_index] = right_item
            right_index += 1

        main_index += 1

    merge_rest_of_half_into_main(
        main=main_list,
        main_index=main_index,
        half=left_half,
        half_index=left_index
    )
    merge_rest_of_half_into_main(
        main=main_list,
        main_index=main_index,
        half=right_half,
        half_index=right_index
    )


def merge_sort(input_list):
    list_size = len(input_list)
    if list_size > 1:
        middle = list_size // 2
        left_half = input_list[:middle]
        right_half = input_list[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge_halfs_into_main_list(input_list, left_half, right_half)

    return input_list
