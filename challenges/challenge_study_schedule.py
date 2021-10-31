def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for i,j in permanence_period:
            if i <= target_time <= j:
                counter += 1
        return counter
    except TypeError:
        return None
