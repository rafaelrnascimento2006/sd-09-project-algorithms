# import timeit


def study_schedule(permanence_period, target_time):
    """(n) percorrer uma única vez
    Validações se vem entrada vazia no target_time
    Vem com array com dados invalidos
    1º passo -> criar variavel qtd_students = 0
    2º passo -> validação do taregt, e do permanence_period vai
    ter que ser no formal (if number none ou not int) return None
    3º passo -> Percorrer o array
    Faz a comparação da posição 0 e 1 de cada item
    if o valor esta dentro daquele periodo
    ele soma 1
    """
    if target_time is None:
        return None
    qtd_students = 0
    for item in permanence_period:
        if item[0] is None or item[1] is None:
            qtd_students = None
            break
        elif item[0] <= target_time <= item[1]:
            qtd_students += 1
    return qtd_students


"""
setup_import = (
    "from challenges.challenge_study_schedule " "import study_schedule"
)
time = timeit.timeit(
    "(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 4), (4, 5)], 4))",
    setup=f"{setup_import}",
    number=10000,
)
print(time)
"""


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 4), (4, 5)], 4))
