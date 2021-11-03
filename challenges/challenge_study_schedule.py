def study_schedule(permanence_period, target_time):
    response = 0

    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        elif target_time is None:
            return None
        elif period[0] <= target_time <= period[1]:
            response += 1
    return response


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
