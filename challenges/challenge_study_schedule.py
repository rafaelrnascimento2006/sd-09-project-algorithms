def study_schedule(permanence_period, target_time):
    quantity_of_students = 0
    if type(target_time) != int:
        return None
    for period in permanence_period:
        entrance, exits = period
        if type(entrance) != int or type(exits) != int:
            return None
        if entrance <= target_time <= exits:
            quantity_of_students += 1
    return quantity_of_students
