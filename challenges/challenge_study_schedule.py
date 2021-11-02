def study_schedule(permanence_period, target_time):
    """ Returns the amount of items in permanence_period that contains
    target_time in its interval or None if any of them has an invalid value"""
    count = 0
    try:
        for start, end in permanence_period:
            if start <= target_time <= end:
                count += 1
    except TypeError:
        return None
    return count
