def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0
    for entrance, exit in permanence_period:
        if not entrance or not exit:
            return None

        if entrance <= target_time <= exit:
            counter += 1
    return counter
