def study_schedule(permanence_period, target_time):
    students = 0
    for index_one, index_two in permanence_period:
        try:
            if index_one <= target_time <= index_two:
                students += 1
        except Exception:
            return None
    return students
