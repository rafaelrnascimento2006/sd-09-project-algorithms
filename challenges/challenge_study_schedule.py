def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    contador = 0
    for hours in permanence_period:
        if type(hours[0]) != int or type(hours[1]) != int:
            return None

        if hours[0] <= target_time <= hours[1]:
            contador += 1

    return contador
