def study_schedule(permanence_period, target_time):
    repeat_counter = 0
    for item in permanence_period:
        if type(item[0]) != int or type(item[1]) != int or target_time is None:
            return None
        if item[0] <= target_time <= item[1]:
            repeat_counter += 1
    return repeat_counter
