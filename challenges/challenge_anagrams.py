def order_word(left, right):
    # Implementar lógica de ordenação
    return True


def split_word(word):
    if len(word) <= 1:
        return word

    mid = len(word) // 2
    left, right = split_word(word[:mid]), split_word(word[mid:])

    return order_word(left, right)


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    return split_word(first_string) == split_word(second_string)
