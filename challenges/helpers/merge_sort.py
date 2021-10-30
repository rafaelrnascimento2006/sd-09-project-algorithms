def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]  # variaveis auxiliares
    right = lista[meio:fim]
    index_left, index_right = 0, 0
    for k in range(inicio, fim):
        if index_left >= len(left):  # se não existe aquela posição
            lista[k] = right[index_right]
            index_right = index_right + 1
        elif index_right >= len(right):
            lista[k] = left[index_left]
            index_left = index_left + 1
        elif left[index_left] < right[index_right]:
            lista[k] = left[index_left]
            index_left = index_left + 1
        else:
            lista[k] = right[index_right]
            index_right = index_right + 1
