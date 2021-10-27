def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    matchHorario = 0 # quantas vezes o target time foi encontrado entre o periodo de entrada e saída
    if target_time is None:
        return None
    
    for [horario1, horario2] in permanence_period:
        if (horario1 or horario2) is None:
            return None
        if horario1 <= target_time <= horario2: # target time precisa estar entre os horários para dar o match
            matchHorario += 1 # toda vez que der match do target time entre a hora que o aluno entrou e a hora que saiu 
    return matchHorario

	
arrTuple = [(80, 80), (80, 80), (80, 90), (1, 5), (4, 5), (4, 5)]
hor = 80

print(study_schedule(arrTuple, hor))