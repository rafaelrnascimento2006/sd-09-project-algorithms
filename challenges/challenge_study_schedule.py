def study_schedule(permanence_period, target_time):
    students_qtty = 0
    if not target_time:
        return None
    for (login, logout) in permanence_period:
        if login and logout:
            if login <= target_time <= logout:
                students_qtty += 1
        else:
            return None
    return students_qtty
