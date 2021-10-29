def study_schedule(permanence_period, target_time):
    number_of_students_present = 0

    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                number_of_students_present += 1
        except TypeError:
            return None

    return number_of_students_present
