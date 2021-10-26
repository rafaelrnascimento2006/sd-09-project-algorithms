def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for entrada, saida in permanence_period:
        if type(entrada) != int or type(saida) != int:
            return None
        if entrada <= target_time and target_time <= saida:
            counter += 1
    return counter
