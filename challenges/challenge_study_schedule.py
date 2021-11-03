# Requisito 01
def study_schedule(permanence_period, target_time):
    if not target_time or len(permanence_period) == 0:
        return None

    count = 0

    for entry_period, exit_period in permanence_period:
        if entry_period and exit_period:
            if entry_period <= target_time <= exit_period:
                count += 1
        else:
            return None

    return count
