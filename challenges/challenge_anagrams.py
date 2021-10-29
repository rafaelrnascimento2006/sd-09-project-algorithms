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


def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1


"""
lista = list("perda")
mergesort(lista)
print(lista)
"""
# print(is_anagram("pato", "tapo"))

# Fonte: https://www.youtube.com/watch?v=5prE6Mz8Vh0
