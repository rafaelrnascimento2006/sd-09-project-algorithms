def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count_students = 0
    try:
        for time in permanence_period:
            if time[0] <= target_time <= time[1]:
                count_students += 1
    except TypeError:
        return None

    return count_students
