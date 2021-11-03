def study_schedule(permanence_period, target_time):
    counter = 0
    if type(target_time) != int:
        return None
    for (login, logof) in permanence_period:
        if type(login) != int or type(logof) != int:
            return None
        if login <= target_time <= logof:
            counter += 1
    return counter
