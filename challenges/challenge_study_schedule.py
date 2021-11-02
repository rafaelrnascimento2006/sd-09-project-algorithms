def study_schedule(permanence_period, target_time):
    """ Returns amount of items in permanence_period
    that contains target_time in its interval"""
    try:
        studying_periods = [i for i in permanence_period
                            if i[0] <= target_time <= i[1]]
    except TypeError:
        return None
    return len(studying_periods)
