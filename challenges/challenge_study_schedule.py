def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for tuple in permanence_period:
        if not isinstance(tuple[0], int) or not isinstance(tuple[1], int):
            return None
        elif tuple[0] <= target_time <= tuple[1]:
            counter += 1

    return counter
