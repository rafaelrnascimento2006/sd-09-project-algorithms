"""
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
    if target_time is None:
        return None
    for index, value in enumerate(permanence_period):
        if None in value:
            return None
        acc = 0
        if target_time in list(range(value[0], value[1]+1)):
            acc += 1
    return acc


teste(permanence_period, 4)
 """


def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    x = (word[::-1] == word, low_index)
    if x[1] >= 1:
        return x[0]
    return is_palindrome_recursive(word, low_index + 1, high_index)


wrd = "reviver"

is_palindrome_recursive(wrd, 0, len(wrd)-1)
