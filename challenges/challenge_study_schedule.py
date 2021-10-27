permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
    students = []
    if target_time is None:
        return None
    for begin, end in permanence_period:
        if (not isinstance(begin, int) or not isinstance(end, int)):
            return None
        if (begin <= target_time <= end):
            students.append((begin, end))
    return len(students)
