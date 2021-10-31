def study_schedule(permanence_period, target_time):
    try:
        contador = 0
        for element in permanence_period:
            if element[0] <= target_time <= element[1]:
                contador += 1
        return contador
    except TypeError:
        return None
