def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        high_counter = 0
        for enter, leave in permanence_period:
            if enter <= target_time <= leave:
                high_counter += 1
    except TypeError:
        return None
    return high_counter
