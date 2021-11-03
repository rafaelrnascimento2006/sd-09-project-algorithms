def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for values in permanence_period:
        if type(values[0]) is not int or type(values[1]) is not int:
            return None
        if values[0] <= target_time <= values[1]:
            count += 1
    return count
