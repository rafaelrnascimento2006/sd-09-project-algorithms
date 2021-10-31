def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    
    total = 0

    for item in permanence_period:
        if item[0] is None or item[1] is None:
            return None
        if item[0] <= target_time <= item[1]:
            total += 1

    return total