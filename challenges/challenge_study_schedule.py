def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for (begin, end) in permanence_period:
        if begin and end:
            if begin <= target_time <= end:
                counter += 1
        else:
            return None
    return counter
                