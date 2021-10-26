def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    result = False
    sum_first_word = sum(map(ord, first_string))
    sum_second_string = sum(map(ord, second_string))

    if(sum_first_word == sum_second_string):
        for letter in second_string:
            if(len(first_string) == len(second_string)):
                if(first_string.__contains__(letter)):
                    result = True
                else:
                    result = False
            else:
                result = False

    return result
