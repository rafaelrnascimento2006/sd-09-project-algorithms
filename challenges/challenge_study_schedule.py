def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        count = 0
        for time in permanence_period:
            if time[0] <= target_time and time[1] >= target_time:
                count += 1

        return count
    except TypeError:
        return None
