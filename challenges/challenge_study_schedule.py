def verify_entries(period):
    if type(period[0]) != int or type(period[1]) != int:
        return None
    return True


def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    best_time = 0
    for period in permanence_period:
        if verify_entries(period) is None:
            return None
        if period[0] <= target_time <= period[1]:
            best_time += 1
    return best_time
