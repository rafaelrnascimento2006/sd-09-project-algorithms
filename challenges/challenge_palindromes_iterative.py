def is_palindrome_iterative(word):
    if word == '':
        return False
    mid = len(word) // 2
    for index in range(0, mid):
        if word[index] != word[-(index + 1)]:
            return False
    return True
