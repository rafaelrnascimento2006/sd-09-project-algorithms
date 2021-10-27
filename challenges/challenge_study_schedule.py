def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for student_permanence in permanence_period:
            if student_permanence[0] <= target_time and \
                student_permanence[1] >= target_time:
                    count += 1
    except TypeError:
        return None
    return count
