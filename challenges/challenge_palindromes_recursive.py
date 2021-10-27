def is_palindrome_recursive(word, low_index, high_index):
    # INPUT: string, int, int
    # OUTPUT: boolean

    # determinar caso base
    #   CASO 1: se a string for vazia OU se os caracteres forem diferentes
    #   CASO 2: se chegar no meio da string e as letras forem iguais
    # chamar a propria funcao atualizando os indices

    if len(word) == 0 or word[low_index] != word[high_index]:
        return False
    if high_index == (len(word)//2):
        return True
    return is_palindrome_recursive(word, low_index+1, high_index-1)
