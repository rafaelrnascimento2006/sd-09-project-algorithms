from challenges.mergesort import merge_sort


def is_anagram(first_string, second_string):
    """
    INPUT: string, string
    OUTPUT: boolean
    PROCEDURE:
        1 - implementar algoritmo de ordenação com complexidade O(n log n)
        2 - ordenar as duas strings
        3 - comparar se as strings sao iguais
                retorna True se forem iguais (É ANAGRAMA)
                OU False se forem diferentes (NÃO É ANAGRAMA)
    """

    first_word = merge_sort(list(first_string))
    second_word = merge_sort(list(second_string))

    print('\n============== DEBUG ==================')
    print(f'first word: {first_word}')
    print(f'second word: {second_word}')
    print('\n===================+++=================')