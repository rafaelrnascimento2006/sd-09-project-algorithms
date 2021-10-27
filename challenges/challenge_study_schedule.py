def study_schedule(permanence_period, target_time):
    if isinstance(target_time, int):
        try:
            periods_match = [
                (start_time, end_time)
                for start_time, end_time in permanence_period
                if start_time <= target_time <= end_time
            ]
            return len(periods_match)
        except TypeError:
            pass
    return None
