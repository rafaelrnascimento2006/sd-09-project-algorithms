def study_schedule(permanence_period, target_time):
    students_total = 0

    if type(target_time) != int:
        return None

    for period in permanence_period:
        entrance, exit = period

        if type(entrance) != int or type(exit) != int:
            return None

        if entrance <= target_time <= exit:
            students_total += 1

    return students_total
