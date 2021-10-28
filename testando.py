niners = [40, 42, 9, 17, 27]


def inversao(niners):
    if len(niners) == 0:
        return niners
    print(niners)
    resultado = inversao(niners[:len(niners)-1])
    print(resultado)
    print(niners)
    return [niners[-1]] + resultado


a = print(inversao(niners))

permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]


def teste(permanence_period, target_time):
    acc = 0
    for index, value in enumerate(permanence_period):
        temp = list(range(value[0], value[1]+1))
        if None in value:
            return None
        elif target_time is None:
            return None
        if target_time in temp:
            acc += 1
    return acc


teste(permanence_period, 4)
