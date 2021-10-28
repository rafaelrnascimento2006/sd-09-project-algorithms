def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count_target = 0
    for start, end in permanence_period:
        if not(start and end):
            return None
        if start <= target_time <= end:
            count_target += 1
    return count_target
