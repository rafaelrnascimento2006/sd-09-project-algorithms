def is_anagram(first_string, second_string):
    anagram_check = False
    sum_string_1 = sum(map(ord, first_string))
    sum_string_2 = sum(map(ord, second_string))
    if sum_string_1 == sum_string_2:
        for letter in second_string:
            if(len(first_string) == len(second_string)):
                anagram_check = True
            else:
                anagram_check = False
        else:
            anagram_check = False
    return anagram_check
