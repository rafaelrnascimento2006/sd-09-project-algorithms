def study_schedule(permanence_period, target_time):

    better_occurrence = 0

    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                better_occurrence += 1
        except TypeError:
            return None

    return better_occurrence
