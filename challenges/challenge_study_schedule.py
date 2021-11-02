def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for period in permanence_period:
        entry, leave = period
        if entry is None or leave is None:
            return None
        if target_time >= entry and target_time <= leave:
            counter += 1
    return counter
