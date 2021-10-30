def is_palindrome_iterative(word):
    if word == "":
        return False
    x = ""
    for value in word[::-1]:
        x += value
    return x == word
