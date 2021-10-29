def study_schedule(permanence_period, target_time):
    """ Essa função retorna o número de estudantes
        em um determinado horário target_time """

    study_counter = 0

    for period in permanence_period:
        if (not isinstance(period[0], int) or not isinstance(period[1], int) or
                not isinstance(target_time, int)):
            return None

        if (target_time >= period[0] and target_time <= period[1]):
            study_counter += 1

    return study_counter
