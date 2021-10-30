from challenges.helpers.merge_sort import mergesort


def is_anagram(first_string, second_string):
    """1º validações se estring vazia
    2º transforma em lista, usa função mergesort que:
    Vai dividindo de cima pra baixo (dividindo metade, metade recursivamente)
    e depois vai vendo qual que é menor para ordenar e ordena
    3º Faz o join para trasnformar a lista em uma estring novamente
    4º Compara para ver se esta igual, se sim returna True, se não return False
    """
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    list_first_string = list(first_string)
    mergesort(list_first_string)
    first_string = "".join(list_first_string)
    list_second_string = list(second_string)
    mergesort(list_second_string)
    second_string = "".join(list_second_string)
    return first_string == second_string


"""
lista = list("perda")
mergesort(lista)
print(lista)
"""
# print(is_anagram("pato", "tapo"))

# Fonte: https://www.youtube.com/watch?v=5prE6Mz8Vh0
