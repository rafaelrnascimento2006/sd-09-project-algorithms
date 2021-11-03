def mergeSort(array):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        return merge(esquerda, direita, array)
    return array


def merge(esquerda, direita, array):
    contador_esquerda = 0
    contador_direita = 0
    contador_geral = 0
    while contador_esquerda < len(esquerda) and contador_direita < len(
        direita
    ):
        if esquerda[contador_esquerda] < direita[contador_direita]:
            array[contador_geral] = esquerda[contador_esquerda]
            contador_esquerda += 1
        else:
            array[contador_geral] = direita[contador_direita]
            contador_direita += 1
        contador_geral += 1

    while contador_esquerda < len(esquerda):
        array[contador_geral] = esquerda[contador_esquerda]
        contador_esquerda += 1
        contador_geral += 1

    while contador_direita < len(direita):
        array[contador_geral] = direita[contador_direita]
        contador_direita += 1
        contador_geral += 1
    return array


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    first_string_array = list(first_string)
    second_string_array = list(second_string)
    first_string_sorted = mergeSort(first_string_array)
    second_string_sorted = mergeSort(second_string_array)

    for i in range(0, len(first_string)):
        if first_string_sorted[i] != second_string_sorted[i]:
            return False
    return True


# https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/mergesort/
# https://www.geeksforgeeks.org/merge-sort/
# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
# https://www.delftstack.com/pt/howto/python/python-string-to-list/
