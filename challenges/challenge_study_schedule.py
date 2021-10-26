def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time and target_time != 0:
        return None

    COUNTER = 0

    for ACCESS, EXIT in permanence_period:

        if type(ACCESS) != int or type(EXIT) != int:
            return None

        if ACCESS <= target_time <= EXIT:
            COUNTER += 1

    return COUNTER
