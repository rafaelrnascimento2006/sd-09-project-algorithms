def study_schedule(permanence_period, target_time):
    """ Faça o código aqui - Req 01 """
    contador = 0
    for entrada, saida in permanence_period:
        try:
            if entrada <= target_time <= saida:
                contador += 1
        except (TypeError, Exception, ValueError):
            return None

    return contador

    # Dica: use um algoritmo de, no máximo, complexidade O(n)
    # Algoritmo deve utilizar a solução iterativa;  == usa for
    # Caso o target_time passado seja nulo, o valor retornado pela função
    # deve ser None (considere o horário 0 como um horário válido);

    # Uma O(n) significa que o algoritmo é linear:
    # Se aumentamos a entrada em 2x, aumentamos o tempo de execução em 2x;

    # Toda vez que uma pessoa estudante abre o sistema,
    # é cadastrado no banco de dados o horário de entrada.
    # Da mesma forma funciona quando o estudante sai do sistema,
    # é cadastrado no banco de dados o horário de saída.
    # Esses dados estarão contidos em uma lista de tuplas (permanence_period)
    # onde cada tupla representa o período de permanência de um estudante
    # com seu horário de entrada e de saída
