def study_schedule(permanence_period, target_time):
    estudantes = 0
    for pessoa in permanence_period:
        if (
            isinstance(pessoa[0], int)
            and isinstance(pessoa[1], int)
            and target_time is not None
        ):
            if (
                pessoa[0] <= target_time <= pessoa[1]
                and estudantes is not None
            ):
                estudantes += 1
        else:
            estudantes = None
    return estudantes
