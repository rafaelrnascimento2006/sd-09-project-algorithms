def validate_times(permanence_period):
    for time in permanence_period:
        if not isinstance(time[0], int) or not isinstance(time[1], int):
            return None
    return True


def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    result = 0
    validate_times(permanence_period)

    try:
        for time in permanence_period:
            if time[0] <= target_time <= time[1]:
                result += 1
    except TypeError:
        return None
    return result
