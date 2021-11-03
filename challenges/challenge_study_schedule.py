def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # counter = 0
    if type(target_time) != int:
        return None
    for period in permanence_period:
        if (type(period[0]) is not int or type(period[1]) is not int):
            return None