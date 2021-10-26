def study_schedule(permanence_period, target_time):
    best_time = []
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                best_time.append(period)
    except TypeError:
        return None

    return len(best_time)
