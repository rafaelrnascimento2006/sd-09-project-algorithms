permanence_period2 = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

def study_schedule(permanence_period, target_time):
    sum_period = 0
    try:
        for elemento in permanence_period:
          if elemento[0] <= target_time <= elemento[1]:
              sum_period += 1
        return sum_period
    except TypeError:
        return None

# print(study_schedule(permanence_period2, 3))

