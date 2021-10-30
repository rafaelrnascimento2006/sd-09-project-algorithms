def study_schedule(permanence_period, target_time):
    if not target_time or target_time==0:
        return None
    counter = 0
    for period in permanence_period:
        if (isinstance(period[0], int) 
        and isinstance(period[1], int) 
        and isinstance(target_time, int)):
            if int(period[0]) <= int(target_time) <= int(period[1]):
                counter += 1
        else:
            counter = None
    return counter


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period,5))
print(study_schedule(permanence_period,4))
print(study_schedule(permanence_period,3))
print(study_schedule(permanence_period,2))
print(study_schedule(permanence_period,1))
