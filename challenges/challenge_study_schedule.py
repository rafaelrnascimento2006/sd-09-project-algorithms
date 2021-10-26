def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        count = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                count += 1
    except TypeError:
        return None

    return count


# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_periods, None))  # 3
# permanence_periods = [(4, None), ("0", 4)]
# print(study_schedule(permanence_periods, 4))  # 3
# permanence_periods = [(4, None), ("0", 4)]
# print(study_schedule(permanence_periods, 4))  # 3
