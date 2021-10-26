def study_schedule(permanence_period, target_time):
    students = 0

    try:
        for permanence_hours in permanence_period:
            if permanence_hours[0] <= target_time <= permanence_hours[1]:
                students += 1
    except TypeError:
        return None

    return students
