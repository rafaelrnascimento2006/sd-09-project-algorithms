def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for (start, finish) in permanence_period:
        if not(start or finish):
            return None
        if start <= target_time <= finish:
            counter += 1
    return counter
