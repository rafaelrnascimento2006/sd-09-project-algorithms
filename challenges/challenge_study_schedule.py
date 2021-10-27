def study_schedule(permanence_period, target_time):
    student = None
    index = 1
    for period in permanence_period:
        if not isinstance(
            period[0], int) or not isinstance(
                period[1], int) or target_time is None:
            return None

        if period[0] <= target_time <= period[1]:
            student = index
            index += 1
    return student
