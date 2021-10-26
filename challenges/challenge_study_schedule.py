def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for item in permanence_period:
        a, b = item
        if a is None or b is None:
            return None
        if target_time >= a and target_time <= b:
            counter += 1
    return counter
