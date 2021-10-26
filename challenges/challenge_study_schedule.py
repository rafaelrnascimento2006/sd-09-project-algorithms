def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    result = 0
    if not isinstance(target_time, int):
        return None
    try:
        for time in permanence_period:
            if not isinstance(time[0], int) or not isinstance(time[0], int):
                return None
            if time[0] <= target_time <= time[1]:
                result += 1
    except TypeError:
        return None
    return result


# permanence_test = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target = 2

# print(study_schedule(permanence_test, target))