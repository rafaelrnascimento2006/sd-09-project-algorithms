from challenges.is_equal import is_equal
from challenges.mergesort import merge_sort


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


def is_anagram(first_string, second_string):
    first_word = merge_sort(list(first_string))
    second_word = merge_sort(list(second_string))
    return is_equal(first_word, second_word)


""" def test():
    assert is_anagram('amor', 'roma') == True
    assert is_anagram('pedra', 'perda') == True
    assert is_anagram('pato', 'tapo') == True
    assert is_anagram('coxinha', 'empada') == False
    print('Tests finished :)')


test() """
