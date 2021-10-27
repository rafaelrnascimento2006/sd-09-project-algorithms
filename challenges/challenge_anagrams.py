def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (first_string or second_string) in (None, ''):
        return False
    else:
        fstlist=list(first_string)
        sndlist=list(second_string)
        # https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
        for each_letter in range(len(fstlist)-1,0,-1):
            for i in range(each_letter):
                if fstlist[i]>fstlist[i+1]:
                    temp = fstlist[i]
                    fstlist[i] = fstlist[i+1]
                    fstlist[i+1] = temp
        for each_letter in range(len(sndlist)-1,0,-1):
            for i in range(each_letter):
                if sndlist[i]>sndlist[i+1]:
                    temp = sndlist[i]
                    sndlist[i] = sndlist[i+1]
                    sndlist[i+1] = temp

    return fstlist == sndlist

print(is_anagram('amor', 'roma'))