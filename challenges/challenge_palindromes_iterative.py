def is_palindrome_iterative(word):
    if word == '':
        return False
    mid = (len(word) // 2) if len(word) % 2 == 0 else (len(word) // 2) + 1
    for index in range(0, mid):
        if word[index] != word[-abs(index + 1)]:
            return False
    return True
