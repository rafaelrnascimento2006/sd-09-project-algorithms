def study_schedule(permanence_period, target_time):
    number_of_students = 0
    if type(target_time) != int:
        return None
    for (entry, exit) in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None
        if entry <= target_time <= exit:
            number_of_students += 1
    return number_of_students
