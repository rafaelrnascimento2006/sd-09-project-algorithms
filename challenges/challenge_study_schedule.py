def is_studying(entry, exit, target_time):
    return entry <= target_time <= exit


def study_schedule(permanence_period, target_time):
    students = 0
    for entry, exit in permanence_period:
        if not entry or not exit or not target_time:
            return None
        if is_studying(entry, exit, target_time):
            students += 1
    return students
