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
    