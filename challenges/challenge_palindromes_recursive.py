def is_palindrome_recursive(word, low_index, high_index):
    """1º validações se len(word) == 0 return false
    2ª verificar o inicio e o fim se são iguais
    3º se for igual chamar a função novamente
    passando inicio +1 e final -1
    - se algum momento não for igual return false
    """
    if len(word) == 0:
        return False
    if word[low_index] == word[high_index]:
        if low_index + 1 > high_index - 1:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
