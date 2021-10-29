def is_palindrome_iterative(word):
    """1º validação se string veio vazia, se sim return False
    2º percorrer e comparar se a letra do inicio é igual a do fim
    de forma iterativa,se sim, fazer até
    a posição da letra inicial ser maior que a posição da final e retun True
    se nao return False
    """
    if len(word) == 0:
        return False
    first_index = 0
    end_index = len(word) - 1
    while first_index < end_index:
        if word[first_index] != word[end_index]:
            return False
        first_index += 1
        end_index -= 1
    return True


# print(is_palindrome_iterative("reviver"))
