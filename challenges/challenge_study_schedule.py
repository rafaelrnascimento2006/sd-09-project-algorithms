def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if type(target_time) != int:
        return None
    for time_period in permanence_period:
        arrival, departure = time_period
        if type(entrance) != int or type(exits) != int:
            return None
        if entrance <= target_time <= exits:
            counter += 1
    return counter