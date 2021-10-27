def study_schedule(permanence_period, target_time):
    if permanence_period is None or target_time is None:
        return None

    counter = 0
    for time_in, out in permanence_period:
        if isinstance(time_in, int) is False or isinstance(out, int) is False:
            return None
        if time_in <= target_time <= out:
            counter += 1
    return counter


if __name__ == '__main__':
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 2))
