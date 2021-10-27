from typing import Counter


def study_schedule(permanence_period, target_time):
    if permanence_period == None or target_time == None:
        return None

    counter = 0
    for time_in, time_out in permanence_period:
        if isinstance(time_in, int) is False or isinstance(time_out, int) is False:
            return None
        if time_in <= target_time <= time_out:
            counter += 1
    return counter


if __name__ == '__main__':
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(permanence_period, 2))