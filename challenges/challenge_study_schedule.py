def study_schedule(permanence_period, target_time):

    """ Faça o código aqui. """
    matchHorario = 0
    if target_time is None:
        return None
    for [horario1, horario2] in permanence_period:
        if not (horario1 or horario2):
            return None
        if horario1 <= target_time <= horario2:
            matchHorario += 1
    return matchHorario

# arrTuple = [(80, 80), (80, 80), (80, 90), (1, 5), (4, 5), (4, 5)]
# hor = 80

# print(study_schedule(arrTuple, hor)) # esperado 3
