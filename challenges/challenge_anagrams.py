# refazendo código req3 em face da determinação de não poder pegar lib pronta
# embora haja certa dúvida se o [::1] se encaixaria nisso

def is_anagram(first_string, second_string):
    if not first_string:
        return False

    if not second_string:
        return False

# como converter string em array em Python
# https://www.delftstack.com/pt/howto/python/python-string-to-list/
    list_first_string = list(first_string)
    list_second_string = list(second_string)

    quicksort(list_first_string, 0, len(list_first_string) - 1)
    quicksort(list_second_string, 0, len(list_second_string) - 1)

    for i in range(len(list_first_string)):
        if list_first_string[i] == list_second_string[i]:
            are_anagrams = True
        else:
            return False
    return are_anagrams


# implementação conforme Course
def quicksort(array, low, high):
    # caso base: se já atingiu a menor porção (1)
    if len(array) == 1:
        # retorne o array
        return array

    # os índices irão se cruzar quando o array estiver ordenado
    if low < high:
        # índice da partição é o índice onde o array foi divido
        # e é determinado a partir do pivô.
        # Este índice já está ordenado
        partition_index = partition(array, low, high)

        # Ordena os elementos presentes antes da partição (menores que o pivô)
        # e depois (maiores que o pivô)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados
def partition(array, low, high):
    # índice do menor elemento
    i = low - 1
    # o pivô será escolhido
    # através do índice que divide o array
    pivot = array[high]  # pivot

    # itera sobre os elementos
    for j in range(low, high):

        # se o elemento corrente é menor ou igual ao pivô
        if array[j] <= pivot:

            # incrementa o índice do menor elemento
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
