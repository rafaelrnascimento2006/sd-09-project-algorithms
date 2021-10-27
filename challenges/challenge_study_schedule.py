def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for element in permanence_period:
            if element[0] <= target_time and element[1] >= target_time:
                count += 1
        return count
    except (TypeError, ValueError):
        return None
    

