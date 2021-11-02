def is_anagram(first_string, second_string):
    """ Faça o código aqui. """


    if len(first_string) != len(second_string):

        return False
    
    splitWord =[]

    for letter in first_string:
        splitWord.append(letter)



    if letter in second_string:
            return True
    else:
            return False   

