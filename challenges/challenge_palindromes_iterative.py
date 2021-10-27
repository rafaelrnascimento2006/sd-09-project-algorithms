def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    for i in range(len(word)-1):
        if word[i] != word[len(word)-(i+1)]:
            return False
    return True


print(is_palindrome_iterative('a'))
