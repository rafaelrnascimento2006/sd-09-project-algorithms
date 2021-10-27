def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    substring_list = list(word)
    for index in range(len(substring_list)-1):
        if substring_list[index] != substring_list[len((substring_list))-(index+1)]:
            return False
    return True
