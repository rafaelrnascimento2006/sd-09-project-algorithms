def study_schedule(permanence_period, target_time):
    result = 0
    for permanence in permanence_period:
        if type(permanence[0]) is not int or type(permanence[1]) is not int:
            return None
        elif target_time is None:
            return None
        elif permanence[0] <= target_time <= permanence[1]:
            result += 1
    return result
