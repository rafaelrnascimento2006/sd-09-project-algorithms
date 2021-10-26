
# https://www.youtube.com/watch?v=4VqmGXwpLqc
def merge_sort(string):
    if (len(string)) <= 1:
        return string

    middle_point = len(string) // 2

    left_part = merge_sort(string[:middle_point])
    right_part = merge_sort(string[middle_point:])

    return merge_split(left_part, right_part)


def merge_split(left_part, right_part):
    sub_array = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left_part) and right_pointer < len(right_part):
        if left_part[left_pointer] < right_part[right_pointer]:
            sub_array.append(left_part[left_pointer])
            left_pointer += 1
        else:
            sub_array.append(right_part[right_pointer])
            right_pointer += 1

    for index in range(left_pointer, len(left_part)):
        sub_array.append(left_part[index])

    for index in range(right_pointer, len(right_part)):
        sub_array.append(right_part[index])

    return sub_array
