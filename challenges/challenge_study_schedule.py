def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    counter = 0

    for period in permanence_period:
        if (type(period[0]) is not int or type(period[1]) is not int):
            return None
        if (period[0] <= target_time <= period[1]):
            counter += 1

    return counter
