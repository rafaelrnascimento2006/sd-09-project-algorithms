def is_anagram(first_string, second_string):
    list1 = list(first_string)
    list2 = list(second_string)
    if len(list1) != len(list2):
        return False
    for letra in list1:
        if letra not in list2:
            return False
        else:
            return True
