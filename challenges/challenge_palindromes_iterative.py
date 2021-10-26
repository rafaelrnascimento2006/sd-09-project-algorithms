import math


def is_palindrome_iterative(word):
    if word == '':
        return False
    mid = math.ceil(len(word) / 2)
    for index in range(0, mid):
        if word[index] != word[-abs(index + 1)]:
            return False
    return True
