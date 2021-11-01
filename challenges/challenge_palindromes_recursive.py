def is_palindrome_recursive(word, low_index, high_index): #inicio = low_index fim = high_index
    # print(low_index, high_index)
    if word == '':
        return False
    if word[low_index] != word[high_index]:
      return False
    else:
      if len(word)-1 == low_index and high_index == 0:
          return True
    return is_palindrome_recursive(word,low_index + 1, high_index -1)


print(is_palindrome_recursive('arara', 0, 4))

# def eh_palindromo(palavra):
#     palavra = palavra.lower()
#     inicio = 0
#     fim = len(palavra)-1
#     for i in range(len(palavra)//2):
#         if palavra[inicio] != palavra[fim]:
#             return False
#         inicio = inicio + 1
#         fim = fim - 1
#     return True
# print(eh_palindromo('Osso'))


