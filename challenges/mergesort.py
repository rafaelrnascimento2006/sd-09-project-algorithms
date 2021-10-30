# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html


def merge_sort(word):
    if len(word) > 1:
        middle = len(word) // 2
        lefthalf = word[:middle]
        righthalf = word[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        lefthalf_index = 0
        righthalf_index = 0
        main_index = 0

        while lefthalf_index < len(lefthalf) and righthalf_index < len(righthalf):
            if lefthalf[lefthalf_index] < righthalf[righthalf_index]:
                word[main_index] = lefthalf[lefthalf_index]
                lefthalf_index += 1
            else:
                word[main_index] = righthalf[righthalf_index]
                righthalf_index += 1
            main_index += 1

        while lefthalf_index < len(lefthalf):
            word[main_index] = lefthalf[lefthalf_index]
            lefthalf_index += 1
            main_index += 1

        while righthalf_index < len(righthalf):
            word[main_index] = righthalf[righthalf_index]
            righthalf_index += 1
            main_index += 1

    return word

# word = list('pato')
# print(merge_sort(word))