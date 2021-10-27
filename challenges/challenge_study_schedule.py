def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for tupla in permanence_period:
        if tupla[1] is None:
            return None
        if tupla[1] >= target_time and tupla[0] <= target_time:
            count += 1
    return count
