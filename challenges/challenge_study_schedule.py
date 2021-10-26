def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    sum_stay_in_period = 0

    if(type(target_time) != int):
        return None
    for student in permanence_period:
        try:
            if(target_time >= student[0] and target_time <= student[1]):
                sum_stay_in_period += 1
        except TypeError:
            return None
    return sum_stay_in_period