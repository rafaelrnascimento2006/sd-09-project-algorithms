def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
        return counter
    except TypeError:
        return None
