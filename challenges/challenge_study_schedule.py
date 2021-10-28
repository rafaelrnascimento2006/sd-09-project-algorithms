permanence_period_test = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def study_schedule(permanence_period, target_time):
    if target_time is None or "":
        return None

    students_at_same_time = 0
    # students_at_same_time = sum(
    # student_schedule.count(
    # target_time
    # ) for student_schedule in permanence_period
    # )

    for (entrance_time, exit_time) in permanence_period:
        if not entrance_time or not exit_time:
            return None

        if entrance_time <= target_time <= exit_time:
            students_at_same_time += 1

    return students_at_same_time
