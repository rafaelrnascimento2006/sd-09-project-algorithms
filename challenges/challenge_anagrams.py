def is_anagram(first_string, second_string):
    if not (first_string and second_string) or (len(first_string) != len(second_string)):
        return False
    for i in range(len(first_string) - 1):
        if not second_string.count(first_string[i]):
            return False
    return True

# p1, p2 = 'amrora', 'arrmao'
# print(is_anagram(p1, p2))
