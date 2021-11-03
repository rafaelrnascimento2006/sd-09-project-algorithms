def count_letter(letter, word):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    count = 0
    is_the_same_count = True

    while count < len(first_string):
        for i in range(len(first_string)):
            count_letter_first = count_letter(first_string[i], first_string)
            count_letter_second = count_letter(first_string[i], second_string)
            if count_letter_first == count_letter_second:
                is_the_same_count = True
                count += 1
            else:
                is_the_same_count = False
                break
    return is_the_same_count

# def contains(letter, string):
#     return letter in string


# def is_anagram(first_string, second_string):
#     if len(first_string) != len(second_string):
#         return False
#     result = True
#     position = 0

#     while result and position < len(first_string):
#         if contains(first_string[position], second_string):
#             result = True
#             position += 1
#         else:
#             result = False
#             break
#     return result
