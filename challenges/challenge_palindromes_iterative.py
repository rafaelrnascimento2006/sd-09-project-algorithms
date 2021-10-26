def is_palindrome_iterative(word):
    if not word:
        return False

    mid_point = len(word) // 2

    for index in range(mid_point):
        if word[index] != word[-(index + 1)]:
            return False
    return True
