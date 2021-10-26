def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    student_counter = 0
    try:
        for (start, stop) in permanence_period:
            if start and stop:
                if start <= target_time <= stop:
                    student_counter += 1
            else:
                return None
    except TypeError:
        return None

    return student_counter
