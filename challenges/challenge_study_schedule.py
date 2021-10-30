def study_schedule(permanence_period, target_time):
    if not target_time or target_time == 0:
        return None
    counter = 0
    for period in permanence_period:
        if (isinstance(period[0], int)
            and isinstance(period[1], int)
                and isinstance(target_time, int)):
            if int(period[0]) <= int(target_time) <= int(period[1]):
                counter += 1
        else:
            counter = None
    return counter
