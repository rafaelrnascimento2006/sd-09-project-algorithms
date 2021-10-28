def validate_inputs(beginning, end, time):
    if beginning == None or end == None or time == None:
        return False
    return True


def study_schedule(permanence_period, target_time):
    """
    INPUT:
        LISTA [
            TUPLA (2, 2) -> (horario de entrada, horario de saida)
        ],
        INT -> horario alvo fornecido como parametro

    OUTPUT: INT -> quantidade de alunos que estavam presentes no periodo
        fornecido como parametro

    PROCEDURE:
        inicializar o contador com 0
        percorrer a lista de tuplas
            a cada tupla verificar se o TARGET_TIME esta no intervalo de
            entrada e saida do aluno
                SE tiver no intervalo SOMAR + 1
        retornar a quantidade de alunos presentes no TARGET_TIME
    """
    counter = 0

    for student in permanence_period:
        if not validate_inputs(student[0], student[1], target_time):
            return None
        if target_time >= student[0] and target_time <= student[1]:
            counter += 1

    return counter