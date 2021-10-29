def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    acc = 0
    for value in permanence_period:
        if None in value:
            return None
        if value[0] <= target_time <= value[1]:
            acc += 1
    return acc
