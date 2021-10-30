def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for schedule in permanence_period:
            if schedule[0] <= target_time and schedule[1] >= target_time:
                count += 1
        return count
    except TypeError:
        return None
