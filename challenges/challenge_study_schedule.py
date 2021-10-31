def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    best_content_time = 0
    if target_time is None:
        return None
    for student in permanence_period:
        # student[0] = entry ----- student[1] = exit
        if student[0] is None or student[1] is None:
            return None
        # https://www.hashtagtreinamentos.com/estruturas-condicionais-no-python?gclid=Cj0KCQjw_fiLBhDOARIsAF4khR03xS1-yulKHuCSpjWriiz4d03i6gTtA_kGqeXmz_x-jJfK9ZyORJMaAol1EALw_wcB
        elif student[0] <= target_time <= student[1]:
            best_content_time += 1

    return best_content_time
