def is_anagram(first_string, second_string):
    count = 0
    for i in first_string:
        for j in second_string:
            if i == j:
                count += 1
                break
    if count == len(first_string) == len(second_string):
        return True
    else:
        return False
