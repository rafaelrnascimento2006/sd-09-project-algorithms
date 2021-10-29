def is_palindrome_iterative(word):
    if not word:
        return False

    mid_index = len(word) // 2
    # inverted_word = word[::-1]
    for i in range(mid_index):
        if word[i] != word[-(i + 1)]:
            return False

    return True
