def study_schedule(permanence_period, target_time):
    repeat_counter = 0
    for item in permanence_period:
        try:
            if item[0] <= target_time <= item[1]:
                repeat_counter += 1
        except Exception:
            return None
    return repeat_counter
