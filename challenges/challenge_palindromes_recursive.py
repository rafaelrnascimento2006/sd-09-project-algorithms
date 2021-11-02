def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui - Req 02 """
    if not word or word[low_index] != word[high_index]:
        return False

    if low_index >= high_index:  # Pega o range todo e evita IndexError
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    # Um palíndromo é uma string, uma palavra, em que não faz
    # diferença se ela é lida da esquerda para a direita ou
    # vice-versa, pois ela mantêm o mesmo sentido. Por exemplo, "ABCBA"

    # O algoritmo deve ser feito utilizando a solução recursiva; == usa if
    # Não se preocupe com a analise da complexidade desse algoritmo;
    # Se for passado uma string vazia, retorne False;
