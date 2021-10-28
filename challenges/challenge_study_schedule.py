def study_schedule(permanence_period, target_time):
    acc = 0
    for index, value in enumerate(permanence_period):
        if None in value:
            return None
        elif target_time is None:
            return None
        temp = list(range(value[0], value[1]+1))
        if target_time in temp:
            acc += 1
    return acc
