def study_schedule(permanence_period, target_time):
    """
    @param permanence_period `tuple` `list`
    @param target_time `number`
    iterates over permanence_period tuples and sums if target_time is between tuple numbers
    Returns hits `number`
    """
    hit = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                hit += 1
    except TypeError:
        return None
    return hit
