def is_anagram(first_string, second_string):
    first = [item for item in first_string]
    second = [item for item in second_string]

    for f_element in range(len(first) - 1):
        for i in range(f_element + 1, len(first)):
            if first[f_element] > first[i]:
                first[f_element], first[i] = first[i], first[f_element]

    for s_element in range(len(second) - 1):
        for i in range(s_element + 1, len(second)):
            if second[s_element] > second[i]:
                second[s_element], second[i] = second[i], second[s_element]

    if first == second:
        return True
    return False
