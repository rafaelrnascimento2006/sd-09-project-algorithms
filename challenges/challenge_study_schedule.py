def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    student_counter = 0
    for (start, stop) in permanence_period:
        if start and stop:
            if start <= target_time <= stop:
                student_counter += 1
        else:
            return None
    return student_counter
