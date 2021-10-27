def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (first_string or second_string) in (None, ''):
        return False
    else:
        fstlist=list(first_string)
        sndlist=list(second_string)
        # https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
        # aproveitando que o python já entende o código ASCII para ordernar alfabeticamente
        def shortBubbleSort(thelist):
            letter_will_move = True
            all_letters = len(thelist)-1
            while all_letters > 0 and letter_will_move:
                letter_will_move = False
                for letter_index in range(all_letters):
                    if thelist[letter_index]>thelist[letter_index+1]:
                        letter_will_move = True
                        temp = thelist[letter_index]
                        thelist[letter_index] = thelist[letter_index+1]
                        thelist[letter_index+1] = temp
                all_letters = all_letters-1
            all_letters = len(thelist)-1
        
    shortBubbleSort(fstlist)
    shortBubbleSort(sndlist)

    return fstlist == sndlist
