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
    ele soma
    exemplo( 1,5)
    target_time = 3
    if (inicial[0] >= target_time) && (final[1] <= target_time)
    if (inicial[0] <= target_time <= final[])
    """
    if target_time is None or type(target_time) is not int:
        print(type(target_time))
        return None
    qtd_students = 0
    for item in permanence_period:
        if (item[0] is None or item[1] is None) or (
            type(item[0]) is not int or type(item[1]) is not int
        ):
            return None
        if item[0] <= target_time <= item[1]:
            qtd_students += 1
    return qtd_students


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 4), (4, 5)], 4))
