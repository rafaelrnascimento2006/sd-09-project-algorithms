def replace_in_list(word_in_list, word_index, some_half, half_index):
    while half_index < len(some_half):
        word_in_list[word_index] = some_half[half_index]
        half_index += 1
        word_index += 1


def merge_sort(word_in_list):
    # referências de merge sort encontradas em:
    # https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
    if len(word_in_list) > 1:
        middle = len(word_in_list) // 2
        left_half = word_in_list[:middle]
        right_half = word_in_list[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index, rigth_index, word_index = 0, 0, 0

        # percorre as metades pelos respectivos indices direito e esquerdo
        # compara e substitui na lista principal (ordenando metades)
        while left_index < len(left_half) and rigth_index < len(right_half):
            if left_half[left_index] < right_half[rigth_index]:
                word_in_list[word_index] = left_half[left_index]
                left_index += 1
            else:
                word_in_list[word_index] = right_half[rigth_index]
                rigth_index += 1
            word_index += 1

        # percorre e substitui a metade esquerda na lista principal
        replace_in_list(word_in_list, word_index, left_half, left_index)

        # percorre e substitui a metade direita na lista principal
        replace_in_list(word_in_list, word_index, right_half, rigth_index)
    return word_in_list


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if(len(first_string) != len(second_string)):
        return False
    if (merge_sort(list(first_string)) == merge_sort(list(second_string))):
        return True
    return False
