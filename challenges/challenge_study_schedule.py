def study_schedule(permanence_period, target_time):
    """Busca qual horário possui maior quantidade de acessos."""
    count = 0
    try:
        for permanence in permanence_period:
            if permanence[0] <= target_time and permanence[1] >= target_time:
                count += 1
    except TypeError:
        return None
    return count


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, 2))
