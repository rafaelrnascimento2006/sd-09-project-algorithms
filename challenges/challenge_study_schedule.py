def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None

    for entry_period, exit_period in permanence_period:
        if entry_period and exit_period:
            if target_time >= entry_period and target_time <= exit_period:
                counter += 1
        else:
            return None
    return counter
