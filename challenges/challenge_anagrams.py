def is_anagram(first_string, second_string):
    first = [item for item in first_string]
    second = [item for item in second_string]

    if len(first_string) == len(second_string):
        for f_element in range(len(first_string)):
            for i in range(f_element + 1, len(first_string)):
                if first[f_element] > first[i]:
                    first[f_element], first[i] = first[i], first[f_element]
                if second[f_element] > second[i]:
                    second[f_element], second[i] = second[i], second[f_element]

    if first == second:
        return True
    return False
