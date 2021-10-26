def study_schedule(permanence_period, target_time):
    students = 0

    if target_time is None:
        return None

    tt = target_time

    for begin, end in permanence_period:
        if type(begin) != int or type(end) != int:
            return None
        if tt >= begin and tt <= end:
            students += 1

    return students
