# Requisito 02
def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if len(word) == 1:
        return True

    # Se as letras forem iguais
    if word[low_index] == word[high_index]:
        # Se o LOW_INDEX ou HIGH_INDEX tiverem valores diferentes do tamanho
        # da palavra
        if low_index + 1 != len(word) and high_index != 0:
            # chama a funcao
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return True
    else:
        # Caso as letras sejam diferentes, retorna FALSE
        return False
