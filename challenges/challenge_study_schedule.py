def study_schedule(permanence_period, target_time):
    try:
        return sum(x <= target_time <= y for x, y in permanence_period)
    except TypeError:
        return None
