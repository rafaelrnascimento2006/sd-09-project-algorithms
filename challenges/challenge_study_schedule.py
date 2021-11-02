def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    people_studing = 0

    if target_time:
        for period in permanence_period:
            #print(period)

            if not period[0] or not period[1]:
                return None
            
            if period[0] <= target_time <= period[1]:
                people_studing += 1
        
        return people_studing