def is_anagram(first_string, second_string):
    count = 0
    second_string_aux = second_string
    for i in first_string:
        for j in second_string_aux:
            if i == j:
                count += 1
                second_string_aux = second_string_aux.replace(j, '', 1)
                break
    if count == len(first_string) == len(second_string):
        return True
    else:
        return False
