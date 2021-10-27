def is_palindrome_iterative(word):
    if not word:
        return False
    return all(word[i] == word[-(i + 1)] for i in range(len(word) // 2))
